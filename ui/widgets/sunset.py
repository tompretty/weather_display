from .base import Widget
from .container import ContainerWidget
from .sunset_text_widget import SunsetTimeWidget
from .text import TextWidget
from .vertical_stack import VerticalStackWidget


class SunsetWidget(Widget):
    def __init__(self, data_source):
        self.widget = ContainerWidget(
            size=(264, 176),
            child=VerticalStackWidget(
                padding=5,
                children=[
                    TextWidget(
                        body="Sunset",
                        font_path="./assets/fonts/Roboto-Regular.ttf",
                        font_size=24,
                    ),
                    SunsetTimeWidget(
                        data_source=data_source,
                        font_path="./assets/fonts/Roboto-Medium.ttf",
                        font_size=72,
                    ),
                ],
            ),
        )

    def draw(self, window):
        self.widget.draw(window)
