from flet import *
from app.utils.color_schema import text_color_1, text_color_2


class TextFieldCustom:
    def __init__(
        self,
        label,
        hint_text,
        password=False,
        can_reveal_password=True,
        width=300,
        height=70,
        padding=Padding(8, 10, 8, 20),
        page=Page,
    ):
        self.page = page
        self.is_password = password
        self.can_reveal_password = can_reveal_password

        # Botón de ojo solo si aplica
        self.eye_button = (
            IconButton(
                icon=icons.VISIBILITY_OFF if self.is_password else None,
                icon_color=text_color_1,
                tooltip="Mostrar/Ocultar",
                on_click=self.toggle_password,
            )
            if password and can_reveal_password
            else None
        )

        self.text_field = TextField(
            label=label,
            hint_text=hint_text,
            filled=True,
            dense=False,
            border=InputBorder.UNDERLINE,
            password=self.is_password,
            can_reveal_password=False,  # Control manual
            width=width,
            height=height,
            content_padding=padding,
            fill_color="#00000000",
            focus_color="0xd91e2e",
            text_style=TextStyle(color=text_color_1, size=16, weight=FontWeight.W_500),
            label_style=TextStyle(color=text_color_1),
            hint_style=TextStyle(color=text_color_1),
            on_focus=self.focus,
            suffix=self.eye_button,
        )

    def toggle_password(self, e):
        self.is_password = not self.is_password
        self.text_field.password = self.is_password
        self.eye_button.icon = (
            icons.VISIBILITY_OFF if self.is_password else icons.VISIBILITY
        )
        self.text_field.update()
        self.eye_button.update()

    def focus(self, e):
        self.text_field.cursor_color = "0xd91e2e"
        self.text_field.hover_color = "0x00ffffff"
        self.text_field.focused_border_color = "0xd91e2e"
        self.text_field.update()

    def build(self):
        return self.text_field


class TextFieldCustom2(TextField):
    def __init__(
        self,
        hint_text,
        width=300,
        height=50,
    ):
        super().__init__(
            label="",
            fit_parent_size=True,
            hint_text=hint_text,
            filled=True,
            dense=False,
            border=InputBorder.UNDERLINE,
            width=width,
            height=height,
            text_align=TextAlign.CENTER,
        )


class TextFieldCustom3(TextField):
    def __init__(
        self,
        hint_text,
        width=300,
        height=40,
    ):
        super().__init__(
            label="",
            fit_parent_size=True,
            hint_text=hint_text,
            filled=False,
            dense=False,
            border=InputBorder.UNDERLINE,
            width=width,
            height=height,
            text_align=TextAlign.START,
            content_padding=padding.only(10, 10, 10, 3),
            capitalization=TextCapitalization.WORDS,
            bgcolor=Colors.TRANSPARENT,
            color=Colors.BLACK,
            text_style=TextStyle(
                color=Colors.BLACK,
                size=14,
            ),
            hint_style=TextStyle(
                color=Colors.BLACK54,
                size=14,
            ),
            border_color=Colors.BLACK,
            focused_border_color=Colors.BLACK,
            cursor_color=Colors.BLACK,
        )


class SearchTextFieldCustom(TextField):
    def __init__(self, hint_text, on_change, width=300, height=40):
        super().__init__(
            label="",
            fit_parent_size=True,
            hint_text=hint_text,
            filled=True,
            bgcolor="#ffffff",
            color="#000000",
            border_color="#000000",
            border=InputBorder.UNDERLINE,
            width=width,
            height=height,
            text_align=TextAlign.CENTER,
            content_padding=padding.only(10, 10, 10, 3),
            capitalization=TextCapitalization.WORDS,
            on_change=on_change,
            hint_style=TextStyle(color="#000000"),
        )


class SearchTextFieldCustom2(TextField):
    def __init__(self, hint_text, on_change, width=None, height=40, expand=1):
        super().__init__(
            label="",
            fit_parent_size=True,
            hint_text=hint_text,
            filled=True,
            dense=False,
            border=InputBorder.UNDERLINE,
            width=width,
            height=height,
            text_align=TextAlign.CENTER,
            content_padding=padding.only(10, 10, 10, 3),
            capitalization=TextCapitalization.WORDS,
            on_change=on_change,
            expand=expand,
            bgcolor="#ffffff",
            color="#000000",
            text_style=TextStyle(color="#000000", size=16, weight=FontWeight.BOLD),
            hint_style=TextStyle(color="#000000", size=16, weight=FontWeight.BOLD),
            border_color="#000000",
            focused_border_color="#000000",
            cursor_color="#000000",
        )


class PlainTextField(TextField):
    def __init__(
        self,
        hint_text,
        width=200,
        height=150,
    ):
        super().__init__(
            fit_parent_size=True,
            label="",
            hint_text=hint_text,
            hint_style=TextStyle(color="#000000"),
            filled=True,
            dense=False,
            expand=True,
            expand_loose=True,
            border=InputBorder.UNDERLINE,
            width=width,
            height=height,
            text_align=TextAlign.START,
            multiline=True,
            capitalization=TextCapitalization.SENTENCES,
            bgcolor="#fefae9",
            focused_border_color="#000000",
            border_color="#000000",
            color="#000000",
        )
