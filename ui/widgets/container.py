from .base import Widget


class ContainerWidget(Widget):
    def __init__(self, size, child, center_x=True, center_y=True, position=(0, 0)):
        super().__init__(position)
        self.size = size
        self.child = child
        self.center_x = center_x
        self.center_y = center_y

    def state(self):
        return self.child.state()

    def set_state(self, state):
        self.child.set_state(state)

    def draw(self, window):
        self.center_child(window)
        self.child.draw(window)

    def center_child(self, window):
        width, height = self.extent(window)
        child_width, child_height = self.child.extent(window)

        if self.center_x:
            center_x = self.x + width / 2
            child_x = int(center_x - child_width / 2)

            self.child.set_x(child_x)

        if self.center_y:
            center_y = self.y + height / 2
            child_y = int(center_y - child_height / 2)

            self.child.set_y(child_y)

    def extent(self, window):
        return self.size
