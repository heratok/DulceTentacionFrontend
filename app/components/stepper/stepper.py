import time
from flet import *

from app.components.stepper.elements.circle import Circle
from app.components.stepper.elements.line import Line


class Stepper(Container):
    def __init__(self, page=Page, content=None, titles=[],):
        super().__init__()
        self.index_step = 1
        self.titles = titles
        self.page = page
        self.widgets = content

        # Elementos del encabezado del Stepper
        self.step1 = Circle(30, page, "1", inited=True)
        self.way1 = Line(page=page, width=300)
        self.step2 = Circle(30, page, "2")
        self.way2 = Line(page=page, width=300)
        self.step3 = Circle(30, page, "3")
        self.button_next = ElevatedButton(
            "Siguiente",
            bgcolor="#D91E2E",
            color="white",
            on_click=lambda e: self.Next(),
            style=ButtonStyle(shape=RoundedRectangleBorder(5))
        )
        self.button_back = ElevatedButton(
            "Volver",
            bgcolor="#D91E2E",
            color="white",
            on_click=lambda e: self.Back(),
            style=ButtonStyle(shape=RoundedRectangleBorder(5))
        )
        self.title = Text(
            self.titles[self.index_step - 1] if self.titles else "Texto descripción",
            weight=FontWeight.BOLD,
            size=25,
            color="black",
            opacity=1,
            animate_opacity=animation.Animation(500, "ease_out"),
        )

        # Crear el Stack de contenido dinámico
        self.content_stack = Stack(
            expand=True,
            controls=[
                Container(
                    content=widget,
                    expand=True,
                    offset=transform.Offset(0 if i == 0 else 1, 0),
                    animate_offset=animation.Animation(500, "ease_in_out"),
                )
                for i, widget in enumerate(content)
            ],
        )

        # Contenedor principal del Stepper
        self.stepper = Container(
            expand=True,
            content=Column(
                controls=[
                    # Título y pasos
                    Container(
                        expand=1,
                        bgcolor="#dfd3b3",
                        border_radius=BorderRadius(15, 15, 0, 0),
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.title,
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    expand=True,
                                    controls=[
                                        self.step1,
                                        self.way1,
                                        self.step2,
                                        self.way2,
                                        self.step3,
                                    ],
                                ),
                            ],
                        ),
                    ),
                    # Contenido dinámico
                    Container(
                        expand=6,
                        bgcolor="#fefae9",
                        border_radius=BorderRadius(0, 0, 15, 15),
                        shadow=BoxShadow(1.5, 10, "0x7f7f7f", (2, 5)),
                        content=self.content_stack,
                    ),
                    # Botones de navegación
                    Container(
                        expand=1,
                        content=Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                self.button_back,
                                self.button_next,
                            ],
                        ),
                    ),
                ]
            ),
        )

    def Back(self):
        if self.index_step == 3:
            self.step3.back()
            time.sleep(.5)
            self.update_text(self.titles[self.index_step-2])

            self.way2.back()

            # añadir la logica para cambiar el contenido del paso

        elif self.index_step == 2:
            self.step2.back()
            time.sleep(.5)
            self.update_text(self.titles[self.index_step-2])

            self.way1.back()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 1:
            # añadir la logica para cambiar el contenido del paso
            pass
        else:
            pass
        if self.index_step > 1:
            self.index_step -= 1
            self.update_content()

    def Next(self):
        if self.index_step == 1:
            self.way1.next()
            self.update_text(self.titles[self.index_step])
            self.update_content()
            time.sleep(.5)
            self.step2.next()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 2:
            self.way2.next()
            self.update_text(self.titles[self.index_step])

            time.sleep(.5)
            self.step3.next()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 3:
            # añadir la logica para cambiar el contenido del paso
            pass
        else:
            pass
        if self.index_step < 3:
            self.index_step += 1
            self.update_content()

    def update_content(self):
        """
        Actualiza los offsets del contenido en el Stack para crear el efecto de deslizamiento.
        """
        for i, widget in enumerate(self.content_stack.controls):
            if i == self.index_step-1:
                widget.offset = transform.Offset(0, 0)  # Centro
            elif i < self.index_step-1:
                widget.offset = transform.Offset(-1, 0)  # Izquierda
            else:
                widget.offset = transform.Offset(1, 0)  # Derecha
            widget.update()

    def update_text(self, new_text):
        """
        Actualiza el título con una animación de opacidad.
        """
        self.title.opacity = 0
        self.title.update()
        self.page.update()
        self.title.value = new_text
        self.title.opacity = 1
        self.title.update()

    def build(self):
        return self.stepper
