from flet import *

from app.components.billing.add_bill import AddBill
from app.components.billing.bill_list_view import BillListView
from app.components.billing.deal_list_view import DealListView
from app.components.billing.open_cash_drawe import OpenCashDrawer
from app.components.custom_button import IconButtonAction
from app.components.dividerCustom import DivCustom
from app.utils.color_schema import *
from app.components.inventory.inventory_replenish import ReplenishInventory


class bill_view(Container):
    def __init__(self, page: Page):
        self.page = page
        self.dlg = AddBill(self.page)
        self.data = [
            {
                "nombre": "Manzanas",
                "ref": "PROD-000001",
                "precio": 41.16,
                "stock": 245,
                "unidad": "cm3",
            },
            {
                "nombre": "Leche",
                "ref": "PROD-000002",
                "precio": 33.08,
                "stock": 403,
                "unidad": "unidades",
            },
            {
                "nombre": "Pan",
                "ref": "PROD-000003",
                "precio": 97.94,
                "stock": 234,
                "unidad": "kilogramos",
            },
            {
                "nombre": "Huevos",
                "ref": "PROD-000004",
                "precio": 70.69,
                "stock": 264,
                "unidad": "kilogramos",
            },
            {
                "nombre": "Arroz",
                "ref": "PROD-000005",
                "precio": 34.59,
                "stock": 37,
                "unidad": "litros",
            },
            {
                "nombre": "Frijoles",
                "ref": "PROD-000006",
                "precio": 5.9,
                "stock": 173,
                "unidad": "unidades",
            },
            {
                "nombre": "Harina",
                "ref": "PROD-000007",
                "precio": 89.24,
                "stock": 286,
                "unidad": "gramos",
            },
            {
                "nombre": "Azúcar",
                "ref": "PROD-000008",
                "precio": 65.88,
                "stock": 273,
                "unidad": "litros",
            },
            {
                "nombre": "Sal",
                "ref": "PROD-000009",
                "precio": 13.79,
                "stock": 284,
                "unidad": "gramos",
            },
            {
                "nombre": "Aceite",
                "ref": "PROD-000010",
                "precio": 31.76,
                "stock": 225,
                "unidad": "cm3",
            },
            {
                "nombre": "Carne de Res",
                "ref": "PROD-000011",
                "precio": 61.2,
                "stock": 191,
                "unidad": "gramos",
            },
            {
                "nombre": "Pescado",
                "ref": "PROD-000012",
                "precio": 86.14,
                "stock": 61,
                "unidad": "kilogramos",
            },
            {
                "nombre": "Pollo",
                "ref": "PROD-000013",
                "precio": 91.71,
                "stock": 430,
                "unidad": "cm3",
            },
            {
                "nombre": "Queso",
                "ref": "PROD-000014",
                "precio": 99.83,
                "stock": 348,
                "unidad": "kilogramos",
            },
            {
                "nombre": "Yogur",
                "ref": "PROD-000015",
                "precio": 21.46,
                "stock": 351,
                "unidad": "unidades",
            },
            {
                "nombre": "Café",
                "ref": "PROD-000016",
                "precio": 54.04,
                "stock": 51,
                "unidad": "unidades",
            },
            {
                "nombre": "Té",
                "ref": "PROD-000017",
                "precio": 16.14,
                "stock": 153,
                "unidad": "litros",
            },
            {
                "nombre": "Cereal",
                "ref": "PROD-000018",
                "precio": 40.67,
                "stock": 345,
                "unidad": "unidades",
            },
            {
                "nombre": "Jugo de Naranja",
                "ref": "PROD-000019",
                "precio": 59.15,
                "stock": 257,
                "unidad": "litros",
            },
            {
                "nombre": "Chocolate",
                "ref": "PROD-000020",
                "precio": 2.38,
                "stock": 426,
                "unidad": "cm3",
            },
        ]
        self.dlgr = ReplenishInventory(self.data, self.page)
        self.dlgo = OpenCashDrawer(self.page, self.openCashDrawer)
        self.monto = 0
        self.monto_text = Text(
            f"$ {self.monto}",
            weight=FontWeight.BOLD,
            size=24,
            text_align=alignment.center,
            color=text_color_1,
        )

    def openCashDrawer(self, monto):
        self.monto = monto
        self.monto_text.value = f"$ {self.monto}"
        self.monto_text.update()

    def build(self):
        """Crea la estructura principal de la vista"""

        return Container(
            content=Column(
                controls=[
                    Container(
                        expand=2,
                        content=Row(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                Container(
                                    bgcolor=Colors.RED_300,
                                    padding=20,
                                    border_radius=BorderRadius(15, 0, 0, 15),
                                    height=130,
                                    width=325,
                                    content=Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Image(
                                                src="static/images/Starting amount.png",  # Enlace a un logo temporal
                                                width=60,
                                                height=60,
                                                fit="contain",
                                            ),
                                            Column(
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    self.monto_text,
                                                    Text(
                                                        "Monto inicial",
                                                        weight=FontWeight.BOLD,
                                                        size=15,
                                                        text_align=alignment.center,
                                                        color=text_color_1,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                Container(
                                    bgcolor=Colors.RED_300,
                                    padding=20,
                                    border_radius=BorderRadius(15, 0, 0, 15),
                                    height=130,
                                    width=325,
                                    content=Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Image(
                                                src="static/images/Sale-icecream.png",  # Enlace a un logo temporal
                                                width=60,
                                                height=60,
                                                fit="contain",
                                            ),
                                            Column(
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    Text(
                                                        "0",
                                                        weight=FontWeight.BOLD,
                                                        size=24,
                                                        text_align=alignment.center,
                                                        color=text_color_1,
                                                    ),
                                                    Text(
                                                        "Ventas",
                                                        weight=FontWeight.BOLD,
                                                        size=15,
                                                        text_align=alignment.center,
                                                        color=text_color_1,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                Container(
                                    bgcolor=Colors.RED_300,
                                    padding=20,
                                    border_radius=BorderRadius(15, 0, 0, 15),
                                    height=130,
                                    width=325,
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                vertical_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    Text(
                                                        "Total en caja",
                                                        weight=FontWeight.BOLD,
                                                        size=15,
                                                        text_align=alignment.center,
                                                        color=text_color_1,
                                                    ),
                                                    Image(
                                                        src="static/images/Stack.png",  # Enlace a un logo temporal
                                                        width=40,
                                                        height=40,
                                                        fit="contain",
                                                    ),
                                                ],
                                            ),
                                            Text(
                                                "$ 850.000,0",
                                                weight=FontWeight.BOLD,
                                                size=28,
                                                text_align=alignment.center,
                                                color=text_color_1,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                    Container(
                        expand=6,
                        content=Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Container(
                                    expand=4,
                                    padding=Padding(20, 20, 20, 0),
                                    content=Column(
                                        expand=1,
                                        controls=[
                                            DivCustom("Factura"),
                                            BillListView(self.data, self.page).build(),
                                        ],
                                    ),
                                ),
                                Container(
                                    expand=2,
                                    padding=Padding(20, 20, 20, 0),
                                    content=Column(
                                        expand=1,
                                        spacing=0,
                                        controls=[
                                            DivCustom("Transacciones"),
                                            DealListView(self.data, self.page).build(),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                    Container(
                        expand=1,
                        bgcolor=bg_color,
                        content=Row(
                            controls=[
                                IconButtonAction(
                                    "Registar",
                                    "static/images/bill.png",
                                    on_click=lambda e: self.page.open(self.dlg),
                                ),
                                IconButtonAction(
                                    "Cancelar",
                                    "static/images/bill-cancel.png",
                                    on_click=lambda e: (),
                                ),
                                IconButtonAction(
                                    "Consulltar",
                                    "static/images/bill-search.png",
                                    on_click=lambda e: self.page.open(self.dlgo),
                                ),
                                IconButtonAction(
                                    "Reporte", "static/images/bill-report.png"
                                ),
                                IconButtonAction(
                                    "Abrir caja",
                                    "static/images/opening.png",
                                    30,
                                    on_click=lambda e: self.page.open(self.dlgo),
                                ),
                            ],
                            expand=True,
                            alignment=MainAxisAlignment.CENTER,
                            spacing=50,
                            vertical_alignment=CrossAxisAlignment.START,
                        ),
                        padding=0,
                    ),
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand_loose=True,
                expand=1,
                spacing=0,
            ),
            expand=1,
            bgcolor="white",
            alignment=alignment.center,
        )
