import flet as ft
from app.utils.color_schema import text_color_1, bg_color_2


class ProfileSidebar(ft.Container):
    def __init__(self, user, on_option_click):
        super().__init__(
            bgcolor=bg_color_2,
            width=220,
            padding=16,
            border=ft.border.only(
                left=ft.BorderSide(2, "#9F9E9E"), right=ft.BorderSide(2, "#9F9E9E")
            ),
            content=ft.Column(
                [
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.PERSON, color="#1a1a1a"),
                                ft.Text("Ver mis datos", color="#1a1a1a", size=16),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color="#1a1a1a",
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.Padding(10, 10, 10, 10),
                            elevation=2,
                        ),
                        on_click=lambda _: on_option_click("user_data"),
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Image(
                                    src="static/images/checklist.png",
                                    width=24,
                                    height=24,
                                ),
                                ft.Text("Categorías", color="#1a1a1a", size=16),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color="#1a1a1a",
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.Padding(10, 10, 10, 10),
                            elevation=2,
                        ),
                        on_click=lambda _: on_option_click("categories"),
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Image(
                                    src="static/images/vendor.png", width=24, height=24
                                ),
                                ft.Text("Proveedores", color="#1a1a1a", size=16),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color="#1a1a1a",
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.Padding(10, 10, 10, 10),
                            elevation=2,
                        ),
                        on_click=lambda _: on_option_click("suppliers"),
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Image(
                                    src="static/images/vendedor.png",
                                    width=24,
                                    height=24,
                                ),
                                ft.Text("Empleados", color="#1a1a1a", size=16),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color="#1a1a1a",
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.Padding(10, 10, 10, 10),
                            elevation=2,
                        ),
                        on_click=lambda _: on_option_click("employees"),
                    ),
                ],
                spacing=16,
            ),
        )
