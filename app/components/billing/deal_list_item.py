from flet import *
from app.utils.color_schema import text_color_1


class DealListItem(Card):
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
        self.method_icon = Image(
            "static/images/item bill.png",
            width=40,
            height=40,
            fit=ImageFit.COVER,
            border_radius=10,
        )
        self.serial_value = Text(
            "Serial: ", weight=FontWeight.BOLD, size=10, color=text_color_1
        )
        self.method_value = Text(
            "Bancolombia ", weight=FontWeight.BOLD, size=10, color=text_color_1
        )
        self.total_value = Text(
            "Serial: ", weight=FontWeight.BOLD, size=10, color=text_color_1
        )
        # self.serial_value = Text("Serial: ",weight=FontWeight.BOLD),
        self.setMethodIcon("bancolombia")

    def selected(self):
        if self.on_select:
            self.on_select(self.data)
            print(self.data)

    def setMethodIcon(self, method):
        if method == "bancolombia":
            self.method_icon.src = "static/images/bancolombia.png"
        elif method == "nequi":
            self.method_icon.src = "static/images/nequi.png"
        elif method == "daviplata":
            self.method_icon.src = "static/images/daviplata.png"
        elif method == "efectivo":
            self.method_icon.src = "static/images/cash.png"
        else:
            pass

    def build(self):
        return Card(
            margin=Margin(10, 10, 50, 0),
            shape=RoundedRectangleBorder(15),
            content=Container(
                bgcolor=Colors.TRANSPARENT,
                border_radius=15,
                content=ListTile(
                    mouse_cursor=MouseCursor.CLICK,
                    bgcolor=Colors.RED_200,
                    hover_color=Colors.RED_600,  # "#ff3462",
                    content_padding=0,
                    min_vertical_padding=0,
                    min_leading_width=0,
                    shape=RoundedRectangleBorder(15),
                    title=Container(
                        height=100,
                        content=Row(
                            controls=[
                                Container(
                                    expand=2,
                                    content=Column(
                                        spacing=5,
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            self.method_icon,
                                            self.method_value,
                                        ],
                                    ),
                                ),
                                Container(
                                    expand=3,
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            Text(
                                                "N° Factura",
                                                weight=FontWeight.BOLD,
                                                size=10,
                                                color=text_color_1,
                                            ),
                                            self.serial_value,
                                        ],
                                    ),
                                ),
                                Container(
                                    expand=2,
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            Text(
                                                "Total",
                                                weight=FontWeight.BOLD,
                                                size=10,
                                                color=text_color_1,
                                            ),
                                            self.total_value,
                                        ],
                                    ),
                                ),
                            ]
                        ),
                    ),
                ),
            ),
        )
