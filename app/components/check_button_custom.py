from flet import *
from app.utils.color_schema import text_color_1


class CheckButtonCuston(Checkbox):
    def __init__(self, value=None, label=None, disabled=None):
        super().__init__()
        self.value = value
        self.label = label
        self.disabled = disabled

    def build(self):
        return Checkbox(
            value=self.value,
            label=self.label,
            label_style=TextStyle(color=text_color_1),
            disabled=self.disabled,
            # fill_color="0xffa1a1",
            active_color="0xd91e2e",
            overlay_color="0xffa1a1",
        )
