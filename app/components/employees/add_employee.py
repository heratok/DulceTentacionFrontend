from flet import *
from ...components.text_field import TextFieldCustom3
from ...utils.color_schema import *


class AddEmployee(AlertDialog):
    def __init__(self, page=Page):
        super().__init__()
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(radius=15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.is_editing = False
        self.on_save = None
        self.photo_path = None

        # Campos del formulario
        self.cedula_field = TextFieldCustom3("Cédula", width=220)
        self.nombres_field = TextFieldCustom3("Nombres", width=220)
        self.apellidos_field = TextFieldCustom3("Apellidos", width=220)
        self.email_field = TextFieldCustom3("Correo", width=220)
        self.role_field = TextFieldCustom3("Rol", width=220)
        self.phone_field = TextFieldCustom3("Teléfono", width=220)
        self.direccion_field = TextFieldCustom3("Dirección", width=150)
        self.barrio_field = TextFieldCustom3("Barrio", width=150)
        self.ciudad_field = TextFieldCustom3("Ciudad", width=150)

        # FilePicker para la foto
        self.file_picker = FilePicker(on_result=self.on_file_selected)
        self.photo_preview = Image(
            src="",
            width=80,
            height=80,
            border_radius=40,
            fit=ImageFit.COVER,
            visible=False,
        )
        self.pick_button = ElevatedButton(
            text="Seleccionar Foto",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=lambda e: self.file_picker.pick_files(
                allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg"]
            ),
        )

        # Textos dinámicos
        self.modal_title = Text(
            value="Registrar Empleado",
            size=18,
            color=text_color_2,
            weight=FontWeight.BOLD,
        )

        self.save_button = ElevatedButton(
            text="Guardar",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=self.save_employee,
        )

        self.title = Container(
            bgcolor=color_h1,
            border_radius=BorderRadius(15, 15, 0, 0),
            expand=True,
            width=450,
            content=Row(
                [
                    Image(
                        "static/images/logo.png",
                        width=70,
                        height=40,
                        fit=ImageFit.CONTAIN,
                    ),
                    Container(
                        content=self.modal_title,
                        alignment=alignment.center,
                        expand=True,
                    ),
                    IconButton(
                        icon=icons.CLOSE,
                        icon_color=text_color_2,
                        on_click=self.close_dlg,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=padding.only(left=15, right=10),
            height=70,
        )

        self.content = Container(
            width=500,
            height=500,
            bgcolor="#FEFAE9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=padding.only(top=20, left=20, right=20, bottom=30),
            content=Column(
                [
                    Row(
                        [self.photo_preview],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    self.pick_button,
                    Row(
                        [
                            self.cedula_field,
                            self.nombres_field,
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    Row(
                        [
                            self.apellidos_field,
                            self.email_field,
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    Row(
                        [
                            self.role_field,
                            self.phone_field,
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    Row(
                        [
                            self.direccion_field,
                            self.barrio_field,
                            self.ciudad_field,
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    Container(height=20),
                    Row(
                        [self.save_button],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=12,
            ),
        )
        self.controls = [self.file_picker]
        if self.file_picker not in self.page.overlay:
            self.page.overlay.append(self.file_picker)
            self.page.update()

    def on_file_selected(self, e):
        if e.files and len(e.files) > 0:
            self.photo_path = e.files[0].path
            self.photo_preview.src = self.photo_path
            self.photo_preview.visible = True
            self.page.update()

    def save_employee(self, e):
        data = {
            "cedula": self.cedula_field.value,
            "nombres": self.nombres_field.value,
            "apellidos": self.apellidos_field.value,
            "email": self.email_field.value,
            "role": self.role_field.value,
            "phone": self.phone_field.value,
            "direccion": self.direccion_field.value,
            "barrio": self.barrio_field.value,
            "ciudad": self.ciudad_field.value,
            "photo": self.photo_path,
        }
        if self.on_save:
            self.on_save(data)
        self.close_dlg(e)

    def show_for_edit(self, employee_data, on_save):
        self.is_editing = True
        self.on_save = on_save
        self.modal_title.value = "Editar Empleado"
        self.save_button.text = "Actualizar"
        self.cedula_field.value = employee_data.get("cedula", "")
        self.nombres_field.value = employee_data.get("nombres", "")
        self.apellidos_field.value = employee_data.get("apellidos", "")
        self.email_field.value = employee_data.get("email", "")
        self.role_field.value = employee_data.get("role", "")
        self.phone_field.value = employee_data.get("phone", "")
        self.direccion_field.value = employee_data.get("direccion", "")
        self.barrio_field.value = employee_data.get("barrio", "")
        self.ciudad_field.value = employee_data.get("ciudad", "")
        self.photo_path = employee_data.get("photo", None)
        if self.photo_path:
            self.photo_preview.src = self.photo_path
            self.photo_preview.visible = True
        else:
            self.photo_preview.visible = False
        self.page.update()
        self.page.open(self)

    def show_for_add(self, on_save):
        self.is_editing = False
        self.on_save = on_save
        self.modal_title.value = "Registrar Empleado"
        self.save_button.text = "Guardar"
        self.cedula_field.value = ""
        self.nombres_field.value = ""
        self.apellidos_field.value = ""
        self.email_field.value = ""
        self.role_field.value = ""
        self.phone_field.value = ""
        self.direccion_field.value = ""
        self.barrio_field.value = ""
        self.ciudad_field.value = ""
        self.photo_path = None
        self.photo_preview.visible = False
        self.page.update()
        self.page.open(self)

    def close_dlg(self, e):
        self.open = False
        self.page.update()
