from flet import *
from app.utils.color_schema import text_color_1


class DivCustom(Container):
    def __init__(self, text, align="start", text_size=20):
        self.set_align = self.set_aligment(align)
        super().__init__(
            expand_loose=True,
            content=Row(
                controls=[
                    Text(
                        value=text,
                        weight=FontWeight.BOLD,
                        size=text_size,
                        color=text_color_1,
                    )
                ],
                alignment=self.set_align,
            ),
            border=border.only(bottom=BorderSide(1, Colors.BLACK)),
        )

    def set_aligment(self, align):
        if align == "start":
            return MainAxisAlignment.START
        elif align == "center":
            return MainAxisAlignment.CENTER
        elif align == "end":
            return MainAxisAlignment.END
        else:
            return MainAxisAlignment.START
