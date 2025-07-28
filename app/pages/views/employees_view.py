from flet import *
from ...utils.color_schema import *
from ...components.employees.add_employee import AddEmployee
from ...components.employees.employees_grid import EmployeesGrid


class EmployeesView(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.page = page
        self.data = []
        self.grid = None
        self.dlg = AddEmployee(self.page)

    def add_employee(self, employee_data):
        self.data.append(employee_data)
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def edit_employee(self, employee_data):
        for i, emp in enumerate(self.data):
            if emp["email"] == employee_data["email"]:
                self.data[i] = employee_data
                break
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def open_add_modal(self, e):
        self.dlg.show_for_add(on_save=self.add_employee)

    def open_edit_modal(self, employee_data):
        self.dlg.show_for_edit(employee_data, on_save=self.edit_employee)

    def delete_employee(self, employee_data):
        self.data = [e for e in self.data if e["email"] != employee_data["email"]]
        if self.grid:
            self.grid.items = self.data
            self.grid.loadGrid()
            self.page.update()

    def build(self):
        self.grid = EmployeesGrid(
            self.data,
            self.page,
            on_delete=self.delete_employee,
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
                                "Panel de Configuración de Empleados",
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
                                    tooltip="Agregar Empleado",
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
