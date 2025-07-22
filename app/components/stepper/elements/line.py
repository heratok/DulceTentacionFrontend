
from flet import *


class Line(Container):
    def __init__(self, width=None, height=None, page=None):
        super().__init__()
        self.page = page
        self.width = width
        self.height = height if height is not None else 10
        self.progress_width = 0  # Ancho inicial del progreso

        # Barra de progreso
        self.progress_bar = Container(
            width=self.progress_width,
            height=self.height,
            bgcolor="#D91E2E",
            animate=animation.Animation(500, "ease_out"),  # Animación de 500ms
        )

        # Contenedor general
        self.content = Container(
            width=self.width,
            bgcolor=Colors.GREY_400,
            height=self.height,
            expand=True if self.width is None else False,
            expand_loose=True,
            alignment=alignment.center_left,
            content=Stack(
                controls=[
                    self.progress_bar  # Barra de progreso
                ],  # Siempre comienza desde la izquierda
            ),
        )

    def build(self):
        return self.content

    def next(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(i / 10)

    def back(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(1-(i / 10))

    def update_progress(self, progress: float):
        """
        Actualiza el progreso de la barra.
        :param progress: Un valor entre 0.0 y 1.0 representando el porcentaje.
        """
        self.progress_width = (
            self.content.width or self.page.window.width) * progress
        self.progress_bar.width = self.progress_width  # Actualizar ancho
        self.progress_bar.update()

