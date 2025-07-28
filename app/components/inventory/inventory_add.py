from flet import *

from app.components.custom_button import IconButtonAction
from app.components.dividerCustom import DivCustom
from app.components.text_field import PlainTextField, TextFieldCustom3
from app.models.inventory import Inventory


class AddInventory(AlertDialog):
    def __init__(self, page=Page):
        super().__init__()
        self.inventoryInstance = Inventory()
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.ref = TextFieldCustom3("Referencia", width=200)
        self.name = TextFieldCustom3("Nombre", width=200)
        self.stock_min = TextFieldCustom3("Stock Minimo", width=150)
        self.unid = TextFieldCustom3("unidad", width=100)
        self.category = TextFieldCustom3("Categoria", width=150)
        self.description = PlainTextField("descripcion")
        self.item_per_package = TextFieldCustom3("Item por paquete", width=170)
        self.purchase_price = TextFieldCustom3("Precio de compra", width=170)
        self.purchase_quantity = TextFieldCustom3("Cantidad comprada", width=170)
        self.expiry_date = TextFieldCustom3("Fecha de Vencimiento", width=200)
        # Contenedor para la imagen
        self.image_container = Container(
            width=150,
            height=150,
            border_radius=75,
            border=border.all(color="black", width=1),
            content=Icon(name=Icons.CAMERA, size=50),
        )

        # Selector de archivos
        self.file_picker = FilePicker(on_result=self.load_image)
        self.page.overlay.append(self.file_picker)

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
        self.content = Container(
            content=Column(
                controls=[
                    Container(width=1, height=10),
                    DivCustom("Informacion Basica"),
                    Container(width=1, height=20),
                    Row(
                        controls=[
                            GestureDetector(
                                content=self.image_container,
                                on_tap=lambda e: self.file_picker.pick_files(),
                            ),
                            Container(
                                padding=0,
                                height=150,
                                content=Column(
                                    controls=[
                                        Row(
                                            controls=[self.ref, self.name],
                                            alignment=MainAxisAlignment.CENTER,
                                        ),
                                        Row(
                                            controls=[
                                                self.stock_min,
                                                self.unid,
                                                self.category,
                                            ],
                                            alignment=MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    expand_loose=True,
                                ),
                            ),
                            Container(
                                bgcolor="#fefae9",
                                border=border.all(color="black", width=2),
                                border_radius=8,
                                padding=8,
                                content=self.description,
                            ),
                        ],
                        spacing=40,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Container(width=1, height=40),
                    DivCustom("Informacion del lote del Producto"),
                    Container(width=1, height=20),
                    Row(
                        controls=[
                            self.item_per_package,
                            self.purchase_price,
                            self.purchase_quantity,
                            self.expiry_date,
                        ],
                        spacing=25,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Container(width=1, height=80),
                    IconButtonAction(
                        "Guardar",
                        "static/images/disk.png",
                        on_click=lambda e: self.add_new(),
                    ),
                    Container(width=1, height=40),
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor="#fefae9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=20,
            height=620,
        )

    # Función para cargar la imagen en el contenedor
    def load_image(self, e):
        if self.file_picker.result and self.file_picker.result.files:
            selected_file = self.file_picker.result.files[0].path
            self.image_container.content = Image(src=selected_file, fit="cover")
            self.page.update()

    def add_new(self):
        data = {
            "ref": self.ref.value,
            "name": self.name.value,
            "category": self.category.value,
            "stock_min": int(self.stock_min.value),
            "unit": self.unid.value,
            "description": self.description.value,
            "purchase_quantity": int(self.purchase_quantity.value),
            "items_per_package": int(self.item_per_package.value),
            "purchase_price": int(self.purchase_price.value),
            "expiry_date": self.expiry_date.value,
            "branch_id": "ratQVKAJpFUZNVFzQS1Pqkanvoz2",
        }

        res = self.inventoryInstance.add(data)
        if res:
            self.page.close(self)

    def build(self):
        return super().build()
