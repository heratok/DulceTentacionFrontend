from flet import *
from app.components.text_field import TextFieldCustom
from app.utils.color_schema import *
from app.models.auth import AuthModel


class LoginPage:
    def __init__(self, page=Page):
        self.page = page
        self.close_button = IconButton(
            icon_color=Colors.WHITE,
            icon=icons.CLOSE,
            on_click=lambda e: self.on_close_click(),
            bgcolor=color_h1a,
        )
        self.text_1 = Text(
            "¿Olvido su contraseña?", style=TextStyle(color=text_color_1)
        )
        self.text_button_1 = TextButton(
            style=ButtonStyle(overlay_color=color_h1a),
            content=self.text_1,
            on_hover=self.text_button_on_hover,
        )

    def text_button_on_hover(self, e):
        self.text_1.style.color = text_color_2 if e.data == "true" else text_color_1
        self.text_1.update()

    def on_close_click(self):
        self.page.window.close()

    def build(self):
        user_field = TextFieldCustom(
            label="Usuario", hint_text="Email o nombre de usuario", page=self.page
        ).build()
        password_field = TextFieldCustom(
            label="Contraseña",
            hint_text="Digite su Contraseña",
            password=True,
            can_reveal_password=True,
            page=self.page,
        ).build()

        error_text = Text("", color="red", visible=False)

        def handle_login(e):
            # email = user_field.value
            # password = password_field.value
            # error_text.visible = False
            # error_text.value = ""
            # error_text.update()
            # data, status = AuthModel.login(email, password)
            # if status == 200 and "token" in data:
            #     self.page.go(route="/main")
            # else:
            #     error_text.value = data.get("error", "Error de autenticación")
            #     error_text.visible = True
            #     error_text.update()
            self.page.go(route="/main")

        return View(
            bgcolor=Colors.TRANSPARENT,
            spacing=0,
            route="/login",
            controls=[
                Container(
                    Column(
                        [
                            Container(
                                Row(
                                    [self.close_button],
                                    alignment="end",
                                    expand=True,
                                    height=40,
                                ),
                            ),
                            Image(
                                "static/images/logo.png",
                                width=300,
                                height=170,
                                fit=ImageFit.CONTAIN,
                            ),
                            Container(height=35, width=1),
                            user_field,
                            Container(height=10, width=1),
                            password_field,
                            error_text,
                            Container(height=50, width=1),
                            ElevatedButton(
                                width=150,
                                height=55,
                                style=ButtonStyle(shape=RoundedRectangleBorder(10)),
                                on_click=handle_login,
                                bgcolor=color_h1,
                                content=Text(
                                    "Iniciar Sesion",
                                    style=TextStyle(color=text_color_2),
                                ),
                            ),
                            self.text_button_1,
                            Container(height=15, width=1),
                            Image(
                                "static/images/LogoInnobyte2024SFN.png",
                                width=100,
                                height=100,
                                fit=ImageFit.CONTAIN,
                            ),
                        ],
                        alignment=MainAxisAlignment.START,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        expand=True,
                    ),
                    bgcolor=bg_color,
                    expand=True,
                    border_radius=15,
                    padding=10,
                )
            ],
        )
