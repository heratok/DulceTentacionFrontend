from flet import *

from app.components.custom_button import IconButtonAction
from app.components.custom_grid import CustomGrid
from app.components.products.product_add import AddProduct
from app.components.text_field import SearchTextFieldCustom


class product_view(Container):
    def __init__(self, page: Page):
        self.page = page
        self.dlg = AddProduct(page)
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

    def build(self):
        grid = CustomGrid(self.data, self.page)
        filter = SearchTextFieldCustom(
            "Buscar insumo por nombre", width=500, on_change=lambda e: grid.filter(e)
        )
        return Container(
            content=Column(
                [
                    Text("Productos", size=40),
                    Container(height=20, width=1),
                    filter,
                    Container(height=50, bgcolor="yellow"),
                    grid.build(),
                    Container(
                        height=100,
                        bgcolor="green",
                        content=Row(
                            controls=[
                                IconButtonAction(
                                    "Registar",
                                    "static/images/add-product.png",
                                    on_click=lambda e: self.page.open(self.dlg),
                                ),
                                IconButtonAction(
                                    "Eliminar",
                                    "static/images/delete-product.png",
                                    on_click=lambda e: grid.delete_selected_item(),
                                ),
                                IconButtonAction(
                                    "Reabastecer",
                                    "static/images/design-product.png",
                                    on_click=lambda e: (),
                                ),
                                IconButtonAction(
                                    "Reporte", "static/images/search-product.png"
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
                spacing=0,
            ),
            expand=True,
            bgcolor="black",
            alignment=alignment.center,
        )
