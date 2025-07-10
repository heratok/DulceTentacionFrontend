import flet as ft
from app.utils.color_schema import text_color_1, bg_color_2


class ProfileSidebar(ft.Container):
    def __init__(self, user, on_option_click):
        super().__init__(
            bgcolor=bg_color_2,
            width=220,
            padding=16,
            border_radius=16,
            shadow=ft.BoxShadow(blur_radius=16, color="#00000022"),
            content=ft.Column(
                [
                    ft.Container(
                        border_radius=12,
                        bgcolor="#1a1a1a",
                        padding=ft.padding.symmetric(vertical=2),
                        content=ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON, color="#f5f5f5"),
                            title=ft.Text("Ver mis datos", color="#f5f5f5", size=16),
                            on_click=lambda _: on_option_click("user_data"),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                    ),
                    ft.Container(
                        border_radius=12,
                        bgcolor="#1a1a1a",
                        padding=ft.padding.symmetric(vertical=2),
                        content=ft.ListTile(
                            leading=ft.Image(
                                src="static/images/checklist.png", width=24, height=24
                            ),
                            title=ft.Text("Categorías", color="#f5f5f5", size=16),
                            on_click=lambda _: on_option_click("categories"),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                    ),
                    ft.Container(
                        border_radius=12,
                        bgcolor="#1a1a1a",
                        padding=ft.padding.symmetric(vertical=2),
                        content=ft.ListTile(
                            leading=ft.Image(
                                src="static/images/vendor.png", width=24, height=24
                            ),
                            title=ft.Text("Proveedores", color="#f5f5f5", size=16),
                            on_click=lambda _: on_option_click("suppliers"),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                    ),
                    ft.Container(
                        border_radius=12,
                        bgcolor="#1a1a1a",
                        padding=ft.padding.symmetric(vertical=2),
                        content=ft.ListTile(
                            leading=ft.Image(
                                src="static/images/vendedor.png", width=24, height=24
                            ),
                            title=ft.Text("Empleados", color="#f5f5f5", size=16),
                            on_click=lambda _: on_option_click("employees"),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                    ),
                ],
                spacing=16,
            ),
        )
