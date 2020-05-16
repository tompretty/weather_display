from .base import Widget


class TabbedWidget(Widget):
    def __init__(self, children, position=(0, 0)):
        super().__init__(position)
        self.children = children
        self.current_tab = 0

    def state(self):
        return [self.current_tab, [child.state() for child in self.children]]

    def set_state(self, state):
        self.current_tab = state[0]
        for child, child_state in zip(self.children, state[1:]):
            child.set_state(child_state)

    def draw(self, window):
        self.draw_current_tab(window)
        self.increment_current_tab()

    def draw_current_tab(self, window):
        self.children[self.current_tab].draw(window)

    def increment_current_tab(self):
        self.current_tab = (self.current_tab + 1) % len(self.children)

    def extent(self, window):
        self.children[self.current_tab].extent(window)
