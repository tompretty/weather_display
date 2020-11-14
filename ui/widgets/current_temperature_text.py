from .text import TextWidget


class CurrentTemperatureTextWidget(TextWidget):
    def __init__(self, data_source, font_path, font_size):
        super().__init__("", font_path, font_size, data_source=data_source)

    def draw(self, window):
        self.update_text()
        super().draw(window)

    def extent(self, window):
        self.update_text()
        return super().extent(window)

    def update_text(self):
        temp = round(self.data_source.get_data())
        self.body = "{}°".format(temp)
