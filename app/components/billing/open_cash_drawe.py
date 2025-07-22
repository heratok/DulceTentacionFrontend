from flet import *

from app.components.text_field import TextFieldCustom3


class OpenCashDrawer(AlertDialog):
    def __init__(self, page=Page, action=None):
        super().__init__()
        # self.inventoryInstance = Inventory()
        self.action = action
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.monto = TextFieldCustom3("0,00", width=200)

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
            width=400,
            content=Row(
                [
                    Image(
                        "static/images/logo.png",
                        width=70,
                        height=40,
                        fit=ImageFit.CONTAIN,
                    ),
                    Text(
                        value="Monto Inicial",
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
        self.text_field = TextFieldCustom3("0,00")

        from app.utils.color_schema import bg_color

        self.content = Container(
            height=200,
            bgcolor=bg_color,
            border_radius=BorderRadius(0, 0, 15, 15),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    self.text_field,
                    ElevatedButton(
                        "Abrir Caja",
                        bgcolor="#D91E2E",
                        color="white",
                        on_click=lambda e: self.openCD(e),
                    ),
                ],
            ),
        )

    def openCD(self, e):
        if self.action:
            self.action(self.text_field.value)
        self.page.close(self)

    def build(self):
        return super().build()
