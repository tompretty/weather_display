from .base import Widget


class VerticalStackWidget(Widget):
    def __init__(self, children, position=(0, 0), padding=0):
        super().__init__(position)
        self.children = children
        self.padding = padding

    def draw(self, window):
        self.position_children(window)
        self.draw_children(window)

    def position_children(self, window):
        child_x = self.x
        child_y = self.y
        for child in self.children:
            child.set_y(child_y)
            child.set_x(child_x)

            child_y += child.height(window) + self.padding

    def draw_children(self, window):
        for child in self.children:
            child.draw(window)

    def extent(self, window):
        width = 0
        height = 0
        for child in self.children:
            child_width, child_height = child.extent(window)
            width = max(width, child_width)
            height += child_height

        height += self.padding * (len(self.children) - 1)

        return width, height
