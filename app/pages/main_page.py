import flet as ft
from flet import *


from app.components.menu import menu
from app.components.titlebar import TitleBar
from app.pages.views.bill_view import bill_view
from app.pages.views.inventory_view import inventory_view
from app.pages.views.product_view import product_view
from app.pages.views.setting_view import settings_view
from app.pages.views.home_view import home_view
from app.pages.views.suppliers_view import suppliers_view
from app.pages.views.categories_view import CategoriesView
from app.pages.views.employees_view import EmployeesView
from app.utils.color_schema import *
from app.components.profile_sidebar import ProfileSidebar
from app.pages.views.user_profile_view import UserProfileView


class MainPage(Column):
    def __init__(self, page: Page):
        self.page = page
        self.page.window.width = 600
        self.page.window.height = 400
        self.page.window.maximized = True
        self.page.window.frameless = True
        self.page.padding = 0
        self.content = ft.Column(
            []
        )  # Inicialización directa compatible con Flet 0.26.0
        self.profile_sidebar = None
        self.profile_sidebar_container = ft.Container(visible=False)
        self.user_data = {
            "photo": "static/images/user.png",
            "name": "Bulma Brief",
            "role": "Administrador",
            "id": "8899001122",
            "birthdate": "733-08-18",
            "first_name": "Bulma",
            "last_name": "Brief",
            "email": "bulma@capsulecorp.com",
            "phone": "3104458667",
            "username": "bulmaGenius",
            "password": "bulma123",
            "address": "3. Ciudad del Futuro",
            "neighborhood": "Zona Científica",
            "city": "Valledupar",
            "branch": "Valledupar",
        }
        self.show_profile_edit = False
        self.main_view = self._create_main_view()

    def show_user_profile(self):
        self.content.controls.clear()
        # Estado: mostrar solo resumen
        self.content.controls.append(
            UserProfileView(
                user=self.user_data,
                on_save=lambda e: None,
                on_change_photo=lambda e: None,
                show_details=False,
            ).build(on_ver_mas=self.handle_ver_mas)
        )
        self.content.update()

    def show_user_profile_details(self):
        self.content.controls.clear()
        # Estado: mostrar detalles
        self.content.controls.append(
            UserProfileView(
                user=self.user_data,
                on_save=lambda e: self.show_user_profile(),
                on_change_photo=lambda e: None,
                show_details=True,
            ).build()
        )
        self.content.update()

    # La función show_user_profile_edit y la vista UserProfileEditView ya no son necesarias

    def on_profile_sidebar_option(self, option):
        self.profile_sidebar_container.visible = True
        self.profile_sidebar_container.update()
        if option == "user_data":
            self.show_user_profile()
        elif option == "suppliers":
            self.content.controls.clear()
            self.content.controls.append(suppliers_view(self.page).build())
            self.content.update()
        elif option == "categories":
            self.content.controls.clear()
            self.content.controls.append(CategoriesView(self.page).build())
            self.content.update()
        elif option == "employees":
            self.content.controls.clear()
            self.content.controls.append(EmployeesView(self.page).build())
            self.content.update()

    # Agrega el callback para el botón 'Ver más' en el resumen
    def handle_ver_mas(self, e=None):
        self.show_user_profile_details()

    def on_menu_item_click(self, item):
        self.content.controls.clear()
        if item == "home":
            self.content.controls.append(home_view())
        elif item == "billing":
            self.content.controls.append(bill_view(self.page).build())
        elif item == "inventory":
            self.content.controls.append(inventory_view(self.page).build())
        elif item == "menu":
            self.content.controls.append(product_view(self.page).build())
        elif item == "settings":
            self.content.controls.append(settings_view(self.page).build())
        elif item == "reports":
            self.content.controls.append(ft.Text("Reportes", size=24))
        elif item == "accounting":
            self.content.controls.append(ft.Text("Contabilidad", size=24))
        elif item == "profile_sidebar":
            # Mostrar la vista "Ver mis datos" y mantener visible el sidebar
            if not self.profile_sidebar:
                self.profile_sidebar = ProfileSidebar(
                    self.user_data, self.on_profile_sidebar_option
                )
                self.profile_sidebar_container.content = self.profile_sidebar
            self.profile_sidebar_container.visible = True
            self.profile_sidebar_container.update()
            self.show_user_profile()
            return
        else:
            self.content.controls.append(ft.Text(f"View: {item}", size=24))
        self.profile_sidebar_container.visible = False
        self.profile_sidebar_container.update()
        self.content.update()

    def _create_main_view(self):
        """Crea la estructura principal de la vista"""
        return Column(
            adaptive=True,
            controls=[
                TitleBar(page=self.page).build(),
                Row(
                    [
                        menu(self.on_menu_item_click),
                        self.profile_sidebar_container,
                        Container(
                            content=self.content,
                            expand=True,
                            padding=0,
                            bgcolor=fg_color,
                        ),
                    ],
                    expand=True,
                    spacing=0,
                ),
            ],
            expand=True,
            spacing=0,
        )

    def build(self):
        """Retorna la vista principal"""
        return self.main_view
