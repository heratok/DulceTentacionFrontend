from flet import *
from app.utils.color_schema import text_color_1


class BillListItem(Card):
    def __init__(self, data, page=Page, on_select=None, index=0):
        super().__init__()
        self.page = page
        self.index = index + 1
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

        self.serial_value = Text("Serial: ", weight=FontWeight.BOLD, color=text_color_1)
        self.client_value = Text("Serial: ", weight=FontWeight.BOLD, color=text_color_1)
        self.date_value = Text("Serial: ", weight=FontWeight.BOLD, color=text_color_1)
        self.total_value = Text("Serial: ", weight=FontWeight.BOLD, color=text_color_1)
        # self.serial_value = Text("Serial: ",weight=FontWeight.BOLD),

    def selected(self):
        if self.on_select:
            self.on_select(self.data)
            print(self.data)

    def build(self):
        return Card(
            # padding=5,
            # expand=1,
            # height=200,
            margin=Margin(10, 10, 50, 0),
            shape=RoundedRectangleBorder(15),
            content=Container(
                # margin=5,
                border_radius=15,
                content=ListTile(
                    mouse_cursor=MouseCursor.CLICK,
                    bgcolor=Colors.RED_200,
                    hover_color=Colors.RED_600,  # "#ff3462",
                    content_padding=0,
                    min_vertical_padding=0,
                    min_leading_width=0,
                    shape=RoundedRectangleBorder(0),
                    title=Container(
                        height=100,
                        content=Row(
                            controls=[
                                Container(
                                    expand=1,
                                    content=Column(
                                        spacing=5,
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Image(
                                                "static/images/item bill.png",
                                                width=50,
                                                height=50,
                                                fit=ImageFit.COVER,
                                                border_radius=10,
                                            ),
                                            Text(
                                                f"N° {self.index}",
                                                size=18,
                                                weight=FontWeight.BOLD,
                                                color=text_color_1,
                                            ),
                                        ],
                                    ),
                                ),
                                Container(
                                    expand=6,
                                    content=Row(
                                        controls=[
                                            Container(
                                                expand=1,
                                                padding=10,
                                                content=Column(
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.START,
                                                    spacing=0,
                                                    controls=[
                                                        Row(
                                                            expand_loose=True,
                                                            controls=[
                                                                Text(
                                                                    "Serial: ",
                                                                    weight=FontWeight.BOLD,
                                                                    color=text_color_1,
                                                                ),
                                                                self.serial_value,
                                                            ],
                                                        ),
                                                        Row(
                                                            expand_loose=True,
                                                            controls=[
                                                                Text(
                                                                    "Cliente: ",
                                                                    weight=FontWeight.BOLD,
                                                                    color=text_color_1,
                                                                ),
                                                                self.client_value,
                                                            ],
                                                        ),
                                                        Row(
                                                            expand_loose=True,
                                                            controls=[
                                                                Text(
                                                                    "Fecha: ",
                                                                    weight=FontWeight.BOLD,
                                                                    color=text_color_1,
                                                                ),
                                                                self.date_value,
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Container(
                                                expand=1,
                                                content=Column(
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                    spacing=0,
                                                    controls=[
                                                        Text(
                                                            "Total",
                                                            weight=FontWeight.BOLD,
                                                            color=text_color_1,
                                                        ),
                                                        self.total_value,
                                                    ],
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                Container(
                                    padding=10,
                                    content=IconButton(
                                        Icons.REMOVE_RED_EYE,
                                        icon_size=30,
                                        on_click=lambda x: self.selected(),
                                    ),
                                ),
                            ]
                        ),
                    ),
                ),
            ),
        )
