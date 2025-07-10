import flet as ft
from app.utils.color_schema import color_h1, text_color_1


def UserAvatar(
    user, on_change_photo=None, show_name_and_role=True, show_change_photo=False
):
    controls = [
        ft.Container(
            width=140,
            height=140,
            border_radius=70,
            border=ft.border.all(4, color_h1),
            content=ft.Image(
                src=user.get("photo", "static/images/user.png"),
                width=130,
                height=130,
                border_radius=65,
                fit=ft.ImageFit.COVER,
            ),
        )
    ]
    if show_change_photo and on_change_photo:
        controls.append(
            ft.Container(
                content=ft.ElevatedButton(
                    "Cambiar Foto",
                    bgcolor=color_h1,
                    color="white",
                    on_click=on_change_photo,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=8, bottom=8),
            )
        )
    if show_name_and_role:
        controls.append(
            ft.Container(
                content=ft.Text(
                    f"{user.get('first_name', '')} {user.get('last_name', '')}",
                    size=26,
                    weight="bold",
                    text_align="center",
                    font_family="comicbd",
                    color=text_color_1,
                ),
                padding=ft.padding.only(top=8),
            )
        )
        controls.append(
            ft.Container(
                content=ft.Text(
                    user.get("role", ""),
                    size=18,
                    weight="bold",
                    text_align="center",
                    font_family="comicbd",
                    color=text_color_1,
                ),
                padding=ft.padding.only(bottom=8),
            )
        )
    return ft.Column(
        controls, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4
    )
