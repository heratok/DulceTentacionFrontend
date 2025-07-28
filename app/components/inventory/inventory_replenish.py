from flet import *


from app.components.dividerCustom import DivCustom
from app.components.inventory.bach import BatchView
from app.components.inventory.inventory_replenish_item import ReplenishItemInventory
from app.components.text_field import SearchTextFieldCustom


# class ReplenishInventory(AlertDialog):
#     def __init__(self, items, page=Page):
#         super().__init__()
#         self.page = page
#         self.items = items
#         # self.items_widget = [ReplenishItemInventory(
#         #     item, self.page).build() for item in self.items]
#         # self.listItemsWidget = Container(
#         #     padding=0,
#         #     expand=True,
#         #     content=Column(
#         #         expand=True,
#         #         scroll=ScrollMode.ALWAYS,
#         #         controls=self.items_widget
#         #     )
#         # )
#         # self.data = [
#         #     [1, "Producto A", 10, 20.0, 5, "2025-01-01", "Proveedor A"],
#         #     [2, "Producto B", 15, 25.0, 10, "2025-06-15", "Proveedor B"],
#         # ]
#         # self.bach = BatchView(self.data, self.page)
#         self.title_padding = 0,
#         self.content_padding = 0,
#         self.actions_padding = 0,
#         self.actions = None,
#         self.shape = RoundedRectangleBorder(15),
#         self.title = Container(
#             bgcolor="red",
#             border_radius=BorderRadius(15, 15, 0, 0),
#             expand=True,
#             width=900,
#             content=Row(
#                 [
#                     Image(
#                         "static/images/logo.png",
#                         width=70,
#                         height=40,
#                         fit=ImageFit.CONTAIN
#                     ),
#                     Text(value="Registar Insumo", size=18,
#                          weight=FontWeight.BOLD, color=Colors.WHITE),
#                     Container(height=1, expand=True, bgcolor=Colors.WHITE),
#                     IconButton(
#                         icon_color=Colors.WHITE,
#                         icon=icons.CLOSE,
#                         on_click=lambda x: self.page.close(self)
#                     )
#                 ]
#             )
#         )
#     self.content = Container(
#         bgcolor=Colors.GREEN,
#         border_radius=BorderRadius(0, 0, 15, 15),
#         padding=Padding(20, 0, 20, 20),
#         height=900,
#         expand=True,
#         content=Row(
#             expand=True,
#             controls=[
#                 Container(
#                     border=Border(right=BorderSide(1, Colors.BLACK)),
#                     padding=0,
#                     content=Column(
#                         horizontal_alignment=CrossAxisAlignment.CENTER,
#                         controls=[
#                             Container(width=1, height=10),
#                             Text("Lista de Insumos",
#                                  weight=FontWeight.BOLD, size=20),
#                             SearchTextFieldCustom(
#                                 "Buscar insumo por nombre", width=300, on_change=lambda e: self.search(e.data)),
#                             Container(
#                                 height=1, bgcolor=Colors.BLACK, width=400),
#                             Container(
#                                 bgcolor=Colors.BLUE_600,
#                                 padding=0,
#                                 expand=True,
#                                 content=Column(
#                                     expand=True,
#                                     scroll=ScrollMode.ALWAYS,
#                                     controls=self.listItemsWidget,
#                                 )
#                             )
#                         ]
#                     )
#                 ),
#                 self.bach.build()
#             ]
#         )
#     )

# def loadItems(self):
#     for item in self.items:
#         item_w = ReplenishItemInventory(item, self.page)
#         self.listItemsWidget.content.controls.append(item_w)

# def search(self, text):
#     pass

# def build(self):
#     return super().build()


# from flet import *

# from app.components.custom_button import IconButtonAction
# from app.components.dividerCustom import DivCustom
# from app.components.text_field import PlainTextField, TextFieldCustom3
from app.models.inventory import Inventory


class ReplenishInventory(AlertDialog):
    def __init__(self, items, page=Page):
        super().__init__()
        self.inventoryInstance = Inventory()
        self.page = page
        self.items = items
        self.open = False
        self.shape = RoundedRectangleBorder(15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.item_select = ItemViewSelect(
            data={},
            page=self.page,
        )
        self.item_select_data = None
        self.title = Container(
            bgcolor="red",
            border_radius=BorderRadius(15, 15, 0, 0),
            expand=True,
            width=900,
            content=Row(
                [
                    Image(
                        "static/images/logo.png",
                        width=70,
                        height=40,
                        fit=ImageFit.CONTAIN,
                    ),
                    Text(
                        value="Registar Insumo",
                        size=18,
                        weight=FontWeight.BOLD,
                        color=Colors.WHITE,
                    ),
                    Container(height=1, expand=True, bgcolor=Colors.WHITE),
                    IconButton(
                        icon_color=Colors.WHITE,
                        icon=icons.CLOSE,
                        on_click=lambda x: self.page.close(self),
                    ),
                ]
            ),
        )
        self.listItemsWidget = []
        self.loadItemWidget(self.items)
        self.listitems = Container(
            bgcolor="#dfd3b3",
            padding=0,
            expand=True,
            content=Column(
                expand=True,
                scroll=ScrollMode.ALWAYS,
                controls=self.listItemsWidget,
            ),
        )

        self.data = [
            [1, "Producto A", 10, 20.0, 5, "2025-01-01", "Proveedor A"],
            [2, "Producto B", 15, 25.0, 10, "2025-06-15", "Proveedor B"],
        ]
        self.bach = BatchView(self.data, self.page)
        self.content = Container(
            bgcolor="#fefae9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=Padding(20, 0, 20, 20),
            height=900,
            expand=True,
            content=Row(
                expand=True,
                controls=[
                    Container(
                        border=Border(right=BorderSide(1, Colors.BLACK)),
                        padding=0,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Container(width=1, height=10),
                                Text(
                                    "Lista de Insumos",
                                    weight=FontWeight.BOLD,
                                    size=20,
                                    color="#000000",
                                ),
                                SearchTextFieldCustom(
                                    "Buscar insumo por nombre",
                                    width=300,
                                    on_change=lambda e: self.search(e.data),
                                ),
                                Container(height=1, bgcolor=Colors.BLACK, width=400),
                                self.listitems,
                            ],
                        ),
                    ),
                    Column(
                        expand=True,
                        controls=[
                            DivCustom("Informacion sobre lotes"),
                            self.item_select.build(),
                            DivCustom("Informacion sobre lotes"),
                            self.bach.build(),
                        ],
                    ),
                ],
            ),
        )

    def loadItemWidget(self, list):
        self.listItemsWidget = [
            ReplenishItemInventory(
                item, self.page, on_select=lambda e, item=item: self.select_item(item)
            ).build()
            for item in list
        ]

    def search(self, data):
        filter_items = []
        for item in self.items:
            if data in item["ref"] or data in item["nombre"]:
                filter_items.append(item)

        print(filter_items)
        self.listitems.content.controls.clear()
        self.loadItemWidget(filter_items)
        self.listitems.content.controls.extend(self.listItemsWidget)
        self.listitems.update()
        self.page.update()

    def select_item(self, data):
        self.item_select_data = data
        self.item_select.set_data(data)

    def build(self):
        return super().build()


class ItemViewSelect(Container):
    def __init__(self, data=None, page=Page):
        super().__init__()
        self.page = page
        self.data = data or {}
        self.container = Container(
            padding=Padding(20, 5, 5, 5)
        )  # Contenedor que se actualizará dinámicamente
        self.build_view()

    def set_data(self, data):
        self.data = data
        self.build_view()  # Reconstruye la vista con los nuevos datos
        self.page.update()

    def build_view(self):
        self.container.content = Row(
            controls=[
                Column(
                    controls=[
                        Text(self.data.get("ref", "PROD-XXXXXX"), color="#000000"),
                        Image(
                            "static/images/helado.png",
                            width=100,
                            height=100,
                            fit=ImageFit.COVER,
                            border_radius=10,
                        ),
                        Text(self.data.get("nombre", "Sin nombre"), color="#000000"),
                    ]
                ),
                Column(
                    controls=[
                        Row(
                            controls=[
                                Text("Categoria: ", color="#000000"),
                                Text(
                                    self.data.get("categoria", "null"), color="#000000"
                                ),
                            ]
                        ),
                        Row(
                            controls=[
                                Text("Precio: ", color="#000000"),
                                Text(
                                    str(self.data.get("precio", 0.0)), color="#000000"
                                ),
                            ]
                        ),
                        Row(
                            controls=[
                                Text("Stock: ", color="#000000"),
                                Text(str(self.data.get("stock", 0)), color="#000000"),
                            ]
                        ),
                        Row(
                            controls=[
                                Text("Unidad: ", color="#000000"),
                                Text(
                                    self.data.get("unidad", "unidades"), color="#000000"
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )

    def build(self):
        return self.container


class ReplenishItemInventory(Card):
    def __init__(self, data, page=Page, on_select=None):
        super().__init__()
        self.page = page
        self.data = {
            "nombre": (
                data.get("nombre", "Sin nombre") if data.get("nombre") else "Sin nombre"
            ),
            "ref": data.get("ref", "PROD-XXXXXX") if data.get("ref") else "PROD-XXXXXX",
            "precio": (
                data.get("precio", 0.0)
                if isinstance(data.get("precio"), (int, float))
                else 0.0
            ),
            "stock": data.get("stock", 0) if isinstance(data.get("stock"), int) else 0,
            "unidad": (
                data.get("unidad", "unidades") if data.get("unidad") else "unidades"
            ),
        }
        self.on_select = on_select

    def selected(self):
        if self.on_select:
            self.on_select(self.data)
            print(self.data)

    def build(self):
        return Card(
            margin=Margin(5, 5, 30, 5),
            width=400,
            elevation=5,
            expand=True,
            color=Colors.RED_200,
            content=Container(
                width=400,
                padding=5,
                expand=True,
                content=ListTile(
                    bgcolor=Colors.RED_200,
                    content_padding=0,
                    leading=Image(
                        "static/images/helado.png",
                        width=50,
                        height=50,
                        fit=ImageFit.COVER,
                        border_radius=10,
                    ),
                    title=Text(self.data["nombre"], weight=FontWeight.BOLD),
                    subtitle=Text(self.data["ref"]),
                    trailing=IconButton(
                        Icons.ARROW_RIGHT_ALT_SHARP,
                        icon_size=30,
                        on_click=lambda x: self.selected(),
                    ),
                    width=400,
                ),
            ),
        )
