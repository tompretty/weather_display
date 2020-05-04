from .base import Widget


class TabbedWidget(Widget):
    def __init__(self, children, position=(0, 0)):
        super().__init__(position)
        self.children = children
        self.current_tab = 0

    def draw(self, window):
        self.draw_current_tab(window)
        self.increment_current_tab()

    def draw_current_tab(self, window):
        self.children[self.current_tab].draw(window)

    def increment_current_tab(self):
        self.current_tab = (self.current_tab + 1) % len(self.children)

    def extent(self, window):
        self.children[self.current_tab].extent(window)
