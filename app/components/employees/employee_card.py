from flet import *
from ...utils.color_schema import *


class EmployeeCard(Card):
    def __init__(self, data, page=Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.data = {
            "name": data.get("name", "Sin nombre"),
            "email": data.get("email", ""),
            "role": data.get("role", ""),
            "phone": data.get("phone", ""),
            "photo": data.get("photo", None),
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
                width=200,
                border=border.all(2, color_h1),
                content=Column(
                    [
                        Container(
                            alignment=alignment.center,
                            content=Column(
                                [
                                    Container(
                                        width=100,
                                        height=100,
                                        border_radius=50,
                                        alignment=alignment.center,
                                        border=border.all(3, color_h1),
                                        content=Image(
                                            src=self.data["photo"]
                                            or "static/images/user.png",
                                            width=90,
                                            height=90,
                                            border_radius=45,
                                            fit=ImageFit.COVER,
                                        ),
                                    ),
                                    Text(
                                        self.data["name"],
                                        color=color_h1,
                                        weight=FontWeight.BOLD,
                                        size=22,
                                        text_align=TextAlign.CENTER,
                                    ),
                                    Text(
                                        self.data["role"],
                                        color=colors.BLACK,
                                        weight=FontWeight.BOLD,
                                        size=16,
                                        text_align=TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            padding=padding.only(top=20, bottom=10),
                        ),
                        Row(
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
                        ),
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=0,
                ),
            ),
        )
