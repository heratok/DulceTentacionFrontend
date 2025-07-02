from flet import *
from app.utils.color_schema import *


class SupplierCard(Card):
    def __init__(self, data, page=Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.data = {
            "code": data.get("code", "PROV-XXXXX"),
            "nit": data.get("nit", ""),
            "name": data.get("name", "Sin nombre"),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
        }

    def handle_delete(self, e):
        if self.on_delete:
            self.on_delete(self.data)

    def handle_edit(self, e):
        if self.on_edit:
            self.on_edit(self.data)

    def build(self):
        return Card(
            elevation=0,
            content=Container(
                bgcolor="#FEFAE9",
                border_radius=10,
                width=300,
                content=Column(
                    [
                        # Header rojo con código
                        Container(
                            bgcolor=color_h1,
                            padding=padding.symmetric(horizontal=15, vertical=10),
                            border_radius=border_radius.only(top_left=10, top_right=10),
                            content=Row(
                                [
                                    Text(
                                        self.data["code"],
                                        color=Colors.WHITE,
                                        weight=FontWeight.BOLD,
                                        size=14,
                                    )
                                ]
                            ),
                        ),
                        # Contenido con la información
                        Container(
                            padding=padding.all(15),
                            content=Column(
                                [
                                    Row(
                                        [
                                            Text(
                                                "NIT:",
                                                weight=FontWeight.BOLD,
                                                color=Colors.BLACK,
                                            ),
                                            Text(
                                                self.data["nit"],
                                                color=Colors.BLACK,
                                            ),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "Nombre:",
                                                weight=FontWeight.BOLD,
                                                color=Colors.BLACK,
                                            ),
                                            Text(
                                                self.data["name"],
                                                color=Colors.BLACK,
                                            ),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "Correo:",
                                                weight=FontWeight.BOLD,
                                                color=Colors.BLACK,
                                            ),
                                            Text(
                                                self.data["email"],
                                                color=Colors.BLACK,
                                            ),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "Teléfono:",
                                                weight=FontWeight.BOLD,
                                                color=Colors.BLACK,
                                            ),
                                            Text(
                                                self.data["phone"],
                                                color=Colors.BLACK,
                                            ),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "0",
                                                weight=FontWeight.BOLD,
                                                color=Colors.BLACK,
                                            ),
                                            Text(
                                                "Productos Referenciados",
                                                color=Colors.BLACK,
                                            ),
                                            Image(
                                                src="static/images/add-product.png",
                                                width=20,
                                                height=20,
                                                fit=ImageFit.CONTAIN,
                                            ),
                                        ]
                                    ),
                                    # Botones de acción
                                    Container(
                                        content=Row(
                                            [
                                                IconButton(
                                                    content=Image(
                                                        src="static/images/delete.png",
                                                        width=24,
                                                        height=24,
                                                        fit=ImageFit.CONTAIN,
                                                    ),
                                                    tooltip="Eliminar",
                                                    on_click=self.handle_delete,
                                                ),
                                                IconButton(
                                                    content=Image(
                                                        src="static/images/edit-text.png",
                                                        width=24,
                                                        height=24,
                                                        fit=ImageFit.CONTAIN,
                                                    ),
                                                    tooltip="Editar",
                                                    on_click=self.handle_edit,
                                                ),
                                            ],
                                            alignment=MainAxisAlignment.CENTER,
                                        )
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                ),
            ),
        )
