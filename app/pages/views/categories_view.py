import flet as ft
from ...utils.color_schema import *
from ...components.categories.add_category import AddCategory
from ...components.categories.categories_grid import CategoriesGrid


class CategoriesView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.page = page
        self.data = []
        self.grid = None
        self.dlg = AddCategory(self.page)
        self.load_categorias()

    def load_categorias(self):
        import requests

        try:
            url = "http://localhost:5000/categories"
            resp = requests.get(url)
            if resp.status_code == 200:
                data = resp.json()
                self.data = data.get("categories", [])
            else:
                self.data = []
        except Exception:
            self.data = []

    def add_category(self, category_data):
        import requests

        try:
            url = "http://localhost:5000/categories"
            resp = requests.post(url, json=category_data)
            if resp.status_code == 201:
                self.load_categorias()
                if self.grid:
                    self.grid.items = self.data
                    self.grid.loadGrid()
                    self.page.update()
        except Exception:
            pass

    def edit_category(self, category_data):
        for i, cat in enumerate(self.data):
            if cat["code"] == category_data["code"]:
                self.data[i] = category_data
                break
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def open_add_modal(self, e):
        self.dlg.show_for_add(on_save=self.add_category)

    def open_edit_modal(self, category_data):
        self.dlg.show_for_edit(category_data, on_save=self.edit_category)

    def delete_category(self, category_data):
        self.data = [c for c in self.data if c["code"] != category_data["code"]]
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def build(self):
        self.grid = CategoriesGrid(
            self.data,
            self.page,
            on_delete=self.delete_category,
            on_edit=self.open_edit_modal,
        )
        return ft.Container(
            expand=True,
            bgcolor=bg_color_2,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                "Panel de Configuración de Categorías",
                                size=40,
                                color=text_color_1,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=20),
                    self.grid,
                    ft.Container(
                        height=90,
                        bgcolor="#FEFAE9",
                        content=ft.Row(
                            controls=[
                                ft.FloatingActionButton(
                                    width=70,
                                    height=70,
                                    bgcolor="#D91E2E",
                                    icon=ft.icons.ADD,
                                    tooltip="Agregar Categoría",
                                    on_click=self.open_add_modal,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        shadow=ft.BoxShadow(
                            blur_radius=8, color="#22000000", offset=ft.Offset(0, -2)
                        ),
                        border_radius=ft.border_radius.only(top_left=16, top_right=16),
                    ),
                ],
                expand=True,
            ),
        )
