import flet as ft
from app.utils.color_schema import color_h1, text_color_1


def UserDataForm(user, on_save=None, editable=True):
    return ft.Container(
        width=500,
        bgcolor="#FEFAE9",
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=8, color="#00000011"),
        padding=ft.padding.all(24),
        content=ft.Column(
            [
                ft.Text(
                    "Datos Personales",
                    weight="bold",
                    color=text_color_1,
                    size=14,
                    font_family="comicbd",
                    text_align="left",
                ),
                # Primera fila: Cédula y Fecha de nacimiento
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    "Cédula",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("id", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Nombres",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("first_name", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Correo",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("email", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Usuario",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("username", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.VerticalDivider(width=30, color=color_h1),
                        ft.Column(
                            [
                                ft.Text(
                                    "Fecha de nacimiento",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("birthdate", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Apellidos",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("last_name", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Teléfono",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("phone", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                                ft.Text(
                                    "Contraseña",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("password", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=40,
                ),
                # Segunda fila: Dirección, Barrio, Ciudad
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    "Dirección",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("address", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            expand=True,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Barrio",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("neighborhood", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            expand=True,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Ciudad",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("city", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=20,
                ),
                # Tercera fila: Rol y Sucursal
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    "Rol",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("role", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            expand=True,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Sucursal",
                                    weight="bold",
                                    color=text_color_1,
                                    font_family="comicbd",
                                ),
                                ft.TextField(
                                    value=user.get("branch", ""),
                                    color=text_color_1,
                                    border_color=text_color_1,
                                    border_width=1,
                                    border_radius=0,
                                    text_align="left",
                                    bgcolor="#FEFAE9",
                                    border=ft.InputBorder.UNDERLINE,
                                    read_only=not editable,
                                ),
                            ],
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=20,
                ),
                ft.Container(
                    content=(
                        ft.ElevatedButton(
                            "Guardar",
                            bgcolor=color_h1,
                            color="white",
                            on_click=on_save,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12)
                            ),
                        )
                        if on_save
                        else None
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=16, bottom=16),
                ),
            ],
            spacing=10,
        ),
    )
