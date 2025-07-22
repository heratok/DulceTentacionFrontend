from flet import *

from app.components.stepper.stepper import Stepper
from app.components.stepper.steps.clients import BillingDataClientView
from app.components.stepper.steps.deals import BillingDealView
from app.components.stepper.steps.products import BillingSelectProductView


class AddBill(AlertDialog):
    def __init__(self, page=Page):
        super().__init__()
        # self.inventoryInstance = Inventory()
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        # self.ref = TextFieldCustom3("Referencia", width=200)
        # self.name = TextFieldCustom3("Nombre", width=200)
        # self.stock_min = TextFieldCustom3("Stock Minimo", width=150)
        # self.unid = TextFieldCustom3("unidad", width=100)
        # self.category = TextFieldCustom3("Categoria", width=150)
        # self.description = PlainTextField("descripcion")
        # self.item_per_package = TextFieldCustom3("Item por paquete", width=170)
        # self.purchase_price = TextFieldCustom3("Precio de compra", width=170)
        # self.purchase_quantity = TextFieldCustom3(
        #     "Cantidad comprada", width=170)
        # self.expiry_date = TextFieldCustom3("Fecha de Vencimiento", width=200)
        # Contenedor para la imagen
        self.image_container = Container(
            width=150,
            height=150,
            border_radius=75,
            border=border.all(color="black", width=1),
            content=Icon(name=Icons.CAMERA, size=50),
        )

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
        titles = [
            "Selección de Productos",
            "Datos del Cliente",
            "Opciones de Facturacion",
        ]
        self.product = BillingSelectProductView(page=page)

        self.client = BillingDataClientView(
            page=page,
        )
        self.deal = BillingDealView(
            page=page,
        )
        stepper_content = [self.product.build(), self.client.build(), self.deal.build()]

        self.content = Container(
            bgcolor="#dfd3b3",
            border_radius=BorderRadius(15, 15, 15, 15),
            padding=padding.all(0),
            content=Stepper(
                page=self.page, content=stepper_content, titles=titles
            ).build(),
        )

    def build(self):
        return super().build()
