from flet import *
from app.utils.color_schema import *
from app.components.suppliers.add_supplier import AddSupplier
from app.components.suppliers.suppliers_grid import SuppliersGrid
from app.components.text_field import SearchTextFieldCustom


class suppliers_view(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.page = page
        self.data = []
        self.grid = None
        self.dlg = AddSupplier(self.page)

    def add_supplier(self, supplier_data):
        """Callback para cuando se agrega un nuevo proveedor"""
        self.data.append(supplier_data)
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def edit_supplier(self, supplier_data):
        """Callback para cuando se edita un proveedor"""
        # Encuentra y actualiza el proveedor en la lista
        for i, supplier in enumerate(self.data):
            if supplier["code"] == supplier_data["code"]:
                self.data[i] = supplier_data
                break

        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def open_add_modal(self, e):
        """Abre el modal en modo agregar"""
        self.dlg.show_for_add(on_save=self.add_supplier)

    def open_edit_modal(self, supplier_data):
        """Abre el modal en modo edición"""
        self.dlg.show_for_edit(supplier_data, on_save=self.edit_supplier)

    def delete_supplier(self, supplier_data):
        """Callback para cuando se elimina un proveedor"""
        # Encuentra y elimina el proveedor de la lista
        self.data = [s for s in self.data if s["code"] != supplier_data["code"]]
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def build(self):
        self.grid = SuppliersGrid(
            self.data,
            self.page,
            on_delete=self.delete_supplier,
            on_edit=self.open_edit_modal,
        )

        return Container(
            expand=True,
            bgcolor=bg_color_2,
            content=Column(
                [
                    Row(
                        [
                            Text(
                                "Panel de Configuracion de Proveedores",
                                size=40,
                                color=text_color_1,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Container(height=20),
                    self.grid,
                    Container(
                        height=90,
                        bgcolor="#FEFAE9",
                        content=Row(
                            controls=[
                                FloatingActionButton(
                                    width=70,
                                    height=70,
                                    bgcolor="#D91E2E",
                                    icon=icons.ADD,
                                    tooltip="Agregar Proveedor",
                                    on_click=self.open_add_modal,
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        shadow=BoxShadow(
                            blur_radius=8, color="#22000000", offset=Offset(0, -2)
                        ),
                        border_radius=border_radius.only(top_left=16, top_right=16),
                    ),
                ],
                expand=True,
            ),
        )
