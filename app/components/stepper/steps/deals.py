from flet import *
from app.utils.color_schema import text_color_1

from app.components.check_button_custom import CheckButtonCuston
from app.components.radio_button_custom import RadioButtonCuston


class BillingDealView(Container):
    def __init__(self, page=Page, user=None):
        super().__init__()
        self.user = user
        self.page = page
        # Componentes para tipo de facturación
        self.billing_type = RadioGroup(
            content=Row(
                alignment=MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    RadioButtonCuston(value="normal", label="Facturación Normal").build(),
                    RadioButtonCuston(value="electronica", label="Facturación Electrónica").build()
                ]
            ),
            value="normal"
        )
        # Componentes para métodos de pago
        self.payment_method = RadioGroup(
            content=Row(
                alignment=MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    RadioButtonCuston(value="efectivo", label="Efectivo").build(),
                    RadioButtonCuston(value="nequi", label="Nequi").build(),
                    RadioButtonCuston(value="bancolombia", label="Bancolombia").build(),
                    RadioButtonCuston(value="daviplata", label="DaviPlata").build()
                ]
            )
        )

        # Componentes para notificaciones
        print_checkbox = CheckButtonCuston(label="Imprimir", value=False).build()
        email_checkbox = CheckButtonCuston(
            label="Enviar por Email",
            disabled=False,  # Siempre habilitado para visualización
            value=False
        ).build()
        whatsapp_checkbox = CheckButtonCuston(
            label="Enviar por WhatsApp",
            disabled=False,  # Siempre habilitado para visualización
            value=False
        ).build()

        self.notifications = Row(
            alignment=MainAxisAlignment.SPACE_EVENLY,
            controls=[
                Text("Métodos de notificación:", color=text_color_1),
                print_checkbox,
                email_checkbox,
                whatsapp_checkbox
            ]
        )

    def build(self):
        return Container(
            expand=1,

            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        padding=20,
                        width=700,
                        #bgcolor=colors.AMBER_300,
                        #alignment=alignment.center,
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=20,
                            controls=[

                                Text("Tipo de facturación:", color=text_color_1,
                                     weight=FontWeight.BOLD),
                                self.billing_type,
                                Divider(color=Colors.RED_200),

                                Text("Métodos de pago:", color=text_color_1,
                                     weight=FontWeight.BOLD),
                                self.payment_method,
                                Divider(color=Colors.RED_200),

                                Text("Notificaciones:", weight=FontWeight.BOLD, color=text_color_1),
                                self.notifications
                            ]
                        )
                    ),
                    Container(
                        width=500,
                        bgcolor=colors.TEAL_300,
                    ),
                ]
            )
        )

