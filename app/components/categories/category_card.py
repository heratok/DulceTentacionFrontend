from flet import *
from ...utils.color_schema import *


class CategoryCard(Card):
    def __init__(self, data, page=Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.data = {
            "code": data.get("code", "CAT-XXXXX"),
            "name": data.get("name", "Sin nombre"),
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
                                        color=colors.WHITE,
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
                                                "Nombre:",
                                                weight=FontWeight.BOLD,
                                                color=colors.BLACK,
                                            ),
                                            Text(self.data["name"], color=colors.BLACK),
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
