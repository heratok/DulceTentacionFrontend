from flet import *
from app.utils.color_schema import text_color_1


class RadioButtonCuston(Radio):
    def __init__(self, value=None, label=None):
        super().__init__()
        self.value = value
        self.label = label

    def build(self):
        return Radio(
            value=self.value,
            label=self.label,
            label_style=TextStyle(color=text_color_1),
            # fill_color="0xffa1a1",
            active_color="0xd91e2e",
            overlay_color="0x77ffa1a1",
        )
