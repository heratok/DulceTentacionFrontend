from flet import *

from app.components.products.product_colunm_scroll import  ProductScrollRow
from app.components.text_field import SearchTextFieldCustom2

class BillingSelectProductView(Container):
    def __init__(self, page=Page):
        super().__init__()
        self.page = page
        self.search_text_field = SearchTextFieldCustom2(
            hint_text="Buscar Producto por nombre o referencia...", on_change=lambda e: ())
        data = [
            {"nombre": "Manzanas", "ref": "PROD-000001",
             "precio": 41.16, "stock": 245, "unidad": "cm3"},
            {"nombre": "Leche", "ref": "PROD-000002",
             "precio": 33.08, "stock": 403, "unidad": "unidades"},
            {"nombre": "Pan", "ref": "PROD-000003", "precio": 97.94,
             "stock": 234, "unidad": "kilogramos"},
            {"nombre": "Huevos", "ref": "PROD-000004",
             "precio": 70.69, "stock": 264, "unidad": "kilogramos"},
            {"nombre": "Arroz", "ref": "PROD-000005",
             "precio": 34.59, "stock": 37, "unidad": "litros"},
            {"nombre": "Frijoles", "ref": "PROD-000006",
             "precio": 5.9, "stock": 173, "unidad": "unidades"},
            {"nombre": "Harina", "ref": "PROD-000007",
             "precio": 89.24, "stock": 286, "unidad": "gramos"},
            {"nombre": "Azúcar", "ref": "PROD-000008",
             "precio": 65.88, "stock": 273, "unidad": "litros"},
            {"nombre": "Sal", "ref": "PROD-000009",
             "precio": 13.79, "stock": 284, "unidad": "gramos"},
            {"nombre": "Aceite", "ref": "PROD-000010",
             "precio": 31.76, "stock": 225, "unidad": "cm3"},
            {"nombre": "Carne de Res", "ref": "PROD-000011",
             "precio": 61.2, "stock": 191, "unidad": "gramos"},
            {"nombre": "Pescado", "ref": "PROD-000012",
             "precio": 86.14, "stock": 61, "unidad": "kilogramos"},
            {"nombre": "Pollo", "ref": "PROD-000013",
             "precio": 91.71, "stock": 430, "unidad": "cm3"},
            {"nombre": "Queso", "ref": "PROD-000014", "precio": 99.83,
             "stock": 348, "unidad": "kilogramos"},
            {"nombre": "Yogur", "ref": "PROD-000015",
             "precio": 21.46, "stock": 351, "unidad": "unidades"},
            {"nombre": "Café", "ref": "PROD-000016",
             "precio": 54.04, "stock": 51, "unidad": "unidades"},
            {"nombre": "Té", "ref": "PROD-000017",
             "precio": 16.14, "stock": 153, "unidad": "litros"},
            {"nombre": "Cereal", "ref": "PROD-000018",
             "precio": 40.67, "stock": 345, "unidad": "unidades"},
            {"nombre": "Jugo de Naranja", "ref": "PROD-000019",
             "precio": 59.15, "stock": 257, "unidad": "litros"},
            {"nombre": "Chocolate", "ref": "PROD-000020",
             "precio": 2.38, "stock": 426, "unidad": "cm3"}
        ]
        self.list_products = ProductScrollRow(data, page, self.item_acction)
        self.list_details = BillingSelectProductList(page,self.item_remove)

    def item_remove(self,ref):
        for product in self.list_products.items:
            if product.data['ref'] == ref['ref']:
                product.return_data()
                product.update()
                break
        self.list_details.remove_item_widget(ref['ref'])
        
    def item_acction(self, data):
        self.list_details.add_item_widget(data)
        self.update()

    def build(self):
        return Container(
            expand=1,
            bgcolor="#fefae9",
            border_radius=15,
            content=Column(
                scroll=ScrollMode.ALWAYS,
                expand_loose=True,
                controls=[
                    Container(
                        expand=1,
                        padding=20,
                        bgcolor="#fefae9",
                        border_radius=10,
                        content=self.search_text_field,
                    ),
                    Container(
                        padding=0,
                        expand=5,
                        # No cambiar el color de las cards de productos
                        content=self.list_products.build(),
                    ),
                    Container(
                        expand=5,
                        # Mantener el color original de las cards de productos
                        content=self.list_details.build(),
                    )
                ]
            ),
        )


class BillingSelectProductList(Container):
    def __init__(self, page=Page, delete_action=None):
        super().__init__()
        # self.inventoryInstance = Inventory()
        self.page = page
        self.delete_action = delete_action
        self.items = []
        self.shadow_color = Colors.RED_300
        # self.item_select = ItemViewSelect(data={}, page=self.page,)
        self.item_select_data = None
        self.listItemsWidget = []
        self.content = Container(
            padding=0,
            expand=1,
            # border=Border(left=BorderSide(1,Colors.BLACK)),
            content=Column(
                expand=1,
                scroll=ScrollMode.ALWAYS,
                controls=[item.build() for item in self.listItemsWidget] if len(
                    self.listItemsWidget) != 0 else [],
            )
        )

    def add_item_widget(self, data):
        self.listItemsWidget.append(
            BillingSelectProductListItem(data, self.page,self.delete_action))
        self.content.content.controls = [
            item.build() for item in self.listItemsWidget]
        self.content.update()
        print(len(self.listItemsWidget))

    def remove_item_widget(self, ref):
        aux =[detail  for detail in self.listItemsWidget if detail.data['ref'] != ref]
        self.listItemsWidget.clear()
        self.listItemsWidget.extend(aux)
        self.content.content.controls.clear()
        self.content.content.controls = [
            item.build() for item in self.listItemsWidget]
        self.content.update()
        
        
    def select_item(self, data):
        self.item_select_data = data
        # self.item_select.set_data(data)

    def build(self):
        return self.content


class BillingSelectProductListItem(Container):
    def __init__(self, data=None, page=Page,action=None):
        super().__init__()
        self.page = page
        self. data = data
        self.action = action
        self.count = 1
        self.count_text = Text(self.count, weight=FontWeight.BOLD, size=18)
        self.total_text = Text(
            f"$ {self.data['precio']}", weight=FontWeight.BOLD, size=18)

    def less(self, e):
        if self.count > 1:
            self.count -= 1
            self.count_text.value = self.count
            self.total_text.value = f"$ {round((self.data['precio']*self.count),2)}"
            self.count_text.update()
            self.total_text.update()

    def more(self, e):
        self.count += 1
        self.count_text.value = self.count
        self.total_text.value = f"$ {round((self.data['precio']*self.count),2)}"
        self.count_text.update()
        self.total_text.update()

    def delete(self,e,data):
        if self.action:
            self.action(data)

    def build(self):
        return Container(
            padding=10,
            margin=10,
            bgcolor=Colors.RED_400,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Image(
                                    "static/images/helado.png",
                                    width=75,
                                    height=75,
                                    fit=ImageFit.FILL,
                                    border_radius=10
                                ),
                                Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.START,
                                    spacing=0,
                                    controls=[
                                        Text(
                                            self.data['nombre'], weight=FontWeight.BOLD, size=16),
                                        Text(
                                            self.data['ref'], weight=FontWeight.BOLD, size=10),

                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        
                        content=Row(
                            spacing=25,
                            controls=[
                                Container(
                                    content=Row(
                                        spacing=10,
                                        controls=[
                                            IconButton(
                                                Icons.EXPOSURE_MINUS_1_SHARP,
                                                on_click=self.less,
                                                icon_size=15
                                            ),
                                            self.count_text,
                                            IconButton(
                                                Icons.EXPOSURE_PLUS_1_SHARP,
                                                on_click=self.more,
                                                icon_size=15,
                                            )
                                        ]
                                    )
                                ),
                                self.total_text,
                                IconButton(
                                    Icons.CLOSE_SHARP,
                                    on_click=lambda e:self.delete(e,self.data),
                                    icon_size=15,
                                )
                            ]
                        )
                    ),
                ]
            )
        )



