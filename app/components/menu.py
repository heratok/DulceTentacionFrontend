from app.components.button_menu import ButtonMenu
from ..utils.color_schema import *
import flet as ft


def menu(on_menu_item_click):
    def on_hover(e):
        if e.data == "true":  # Cuando el mouse está sobre el elemento
            container.width = 250  # Expandir el menú
            menu_title_text.opacity = 1  # Mostrar texto "Menu"
            menu_title_text.update()
            for button in menu_buttons:
                button.set_OnHover(True)  # Expandir botones
        else:  # Cuando el mouse sale del elemento
            container.width = 70  # Contraer el menú
            menu_title_text.opacity = 0  # Ocultar texto "Menu"
            menu_title_text.update()
            for button in menu_buttons:
                button.set_OnHover(False)  # Contraer botones
        container.update()  # Actualizar el contenedor

    # Lista de ítems del menú con íconos
    menu_items = [
        {
            "icon": "static/images/heladeria.png",
            "label": "Inicio",
            "on_click": lambda _: on_menu_item_click("home"),
        },
        {
            "icon": "static/images/cajero-automatico.png",
            "label": "Facturacion",
            "on_click": lambda _: on_menu_item_click("billing"),
        },
        {
            "icon": "static/images/menu.png",
            "label": "Productos",
            "on_click": lambda _: on_menu_item_click("menu"),
        },
        {
            "icon": "static/images/fruta.png",
            "label": "Inventario",
            "on_click": lambda _: on_menu_item_click("inventory"),
        },
        {
            "icon": "static/images/budget.png",
            "label": "Contabilidad",
            "on_click": lambda _: on_menu_item_click("accounting"),
        },
        {
            "icon": "static/images/analytics.png",
            "label": "Reportes",
            "on_click": lambda _: on_menu_item_click("reports"),
        },
        {
            "icon": "static/images/vendedor.png",
            "label": "Perfil",
            "on_click": lambda _: on_menu_item_click("profile_sidebar"),
        },
    ]

    # Crear botones del menú
    menu_buttons = [
        ButtonMenu(item["icon"], item["label"], item["on_click"], OnHover=False)
        for item in menu_items
    ]  # Título del menú con ícono y texto animado
    menu_title_text = ft.Text(
        "Menu",
        opacity=0,
        animate_opacity=300,
        size=20,
        weight="bold",
        color=text_color_1,  # Color negro para el título
    )
    menu_title = ft.Row(
        [
            ft.Icon(ft.icons.MENU, size=24),
            menu_title_text,
        ],
        spacing=10,
        alignment="start",
    )

    # Contenedor del menú
    container = ft.Container(
        bgcolor=bg_color_2,
        content=ft.Column(
            expand=True,
            expand_loose=True,
            controls=[
                menu_title,
                ft.Column(
                    [
                        *menu_buttons,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                # Añadir botones del menú
            ],
            alignment="start",
            spacing=16,
        ),
        width=70,  # Ancho inicial (menú contraído)
        padding=8,
        on_hover=on_hover,  # Vincular el evento on_hover
        # Animación suave al cambiar el tamaño
        animate=ft.animation.Animation(500, "ease"),
    )

    return container
