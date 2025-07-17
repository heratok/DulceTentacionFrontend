import flet as ft
from app.components.user import UserAvatar, UserDataForm
from app.components.user.user_profile_title import UserProfileTitle
from app.utils.color_schema import color_h1


class UserProfileView:
    def __init__(self, user, on_save, on_change_photo, show_details=False):
        self.user = user
        self.on_save = on_save
        self.on_change_photo = on_change_photo
        self.show_details = show_details

    def build(self, on_ver_mas=None):
        from app.utils.color_schema import bg_color_2
        if not self.show_details:
            # Modo resumen: mostrar título, nombre y rol, NO botón cambiar foto
            return ft.Container(
                expand=True,
                bgcolor=bg_color_2,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        UserProfileTitle(),
                        UserAvatar(
                            self.user,
                            on_change_photo=self.on_change_photo,
                            show_name_and_role=True,
                            show_change_photo=False,
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Ver más",
                                bgcolor=color_h1,
                                color="white",
                                on_click=on_ver_mas,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12)
                                ),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
            )
        else:
            # Modo detalles: mostrar título, solo foto y botón cambiar foto, NO nombre ni rol
            return ft.Container(
                expand=True,
                bgcolor=bg_color_2,
                alignment=ft.alignment.center,
                content=ft.ListView(
                    expand=True,
                    auto_scroll=False,
                    padding=ft.padding.symmetric(horizontal=0, vertical=10),
                    controls=[
                        UserProfileTitle(),
                        UserAvatar(
                            self.user,
                            on_change_photo=self.on_change_photo,
                            show_name_and_role=False,
                            show_change_photo=True,
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10, left=0, right=0),
                            content=UserDataForm(
                                self.user, on_save=self.on_save, editable=True
                            ),
                        ),
                    ],
                ),
            )
