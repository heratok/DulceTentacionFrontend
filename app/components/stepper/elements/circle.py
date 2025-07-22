


from flet import *


class Circle(Container):
    def __init__(self, size=None, page=None, text="", text_size=12, inited=False):
        super().__init__()
        self.page = page
        self.width = size
        self.height = size
        self.text = text
        self.text_size = text_size
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
            expand=False,
            expand_loose=True,
            border_radius=self.width/2,
            alignment=alignment.center_left,
            content=Stack(
                controls=[
                    self.progress_bar,  # Barra de progreso
                    Container(
                        width=self.width,
                        alignment=alignment.center,
                        height=self.height,
                        padding=0,
                        content=Text(self.text, weight=FontWeight.BOLD, size=self.text_size, color="white"),)
                ],  # Siempre comienza desde la izquierda
            ),
        )
        if inited:
            self.progress_bar.width = self.width

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

