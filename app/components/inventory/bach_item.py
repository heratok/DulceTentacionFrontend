from flet import *


class BatchForm(Container):
    def __init__(self, on_save, on_cancel, form_data=None, page=Page):
        super().__init__()
        self.page = page
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.form_data = form_data or {}

    def build(self):
        # Campos del formulario
        self.id_field = TextField(
            label="ID",
            value=self.form_data.get("id", ""),
            disabled=True,
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.name_field = TextField(
            label="Nombre",
            value=self.form_data.get("name", ""),
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.unit_field = TextField(
            label="Unidad",
            value=self.form_data.get("unit", ""),
            keyboard_type=KeyboardType.NUMBER,
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.price_field = TextField(
            label="Precio",
            value=self.form_data.get("price", ""),
            keyboard_type=KeyboardType.NUMBER,
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.quantity_field = TextField(
            label="Cantidad",
            value=self.form_data.get("quantity", ""),
            keyboard_type=KeyboardType.NUMBER,
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.expiry_date_field = TextField(
            label="Fecha de Vencimiento",
            value=self.form_data.get("expiry_date", ""),
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.supplier_field = TextField(
            label="Proveedor",
            value=self.form_data.get("supplier", ""),
            color="#000000",
            label_style=TextStyle(color="#000000"),
        )
        self.title = Text(
            "Añadir un lote", size=18, weight=FontWeight.BOLD, color="#000000"
        )
        print(self.form_data)
        # Contenedor del formulario
        return Container(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    self.title,
                    Container(width=1, height=10),
                    self.id_field,
                    self.name_field,
                    self.unit_field,
                    self.price_field,
                    self.quantity_field,
                    self.expiry_date_field,
                    self.supplier_field,
                    Container(width=1, height=20),
                    Row(
                        spacing=50,
                        controls=[
                            ElevatedButton(
                                "Guardar",
                                on_click=self.on_save,
                                bgcolor="#d32f2f",
                                color="#ffffff",
                            ),
                            ElevatedButton(
                                "Cancelar",
                                on_click=self.on_cancel,
                                bgcolor="#d32f2f",
                                color="#ffffff",
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                    ),
                ],
            ),
            bgcolor="#fefae9",
            width=400,
            padding=20,
            border_radius=15,
            offset=Offset(3, 0),  # Oculto inicialmente
            animate_offset=Animation(300, AnimationCurve.EASE),
        )
