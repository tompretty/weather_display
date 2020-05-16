class Widget:
    def __init__(self, position):
        self.position = position

    def draw(self, image):
        raise NotImplementedError

    def extent(self, window):
        raise NotImplementedError

    def width(self, window):
        return self.extent(window)[0]

    def height(self, window):
        return self.extent(window)[1]

    def state(self):
        pass

    def set_state(self, state):
        pass

    @property
    def x(self):
        return int(self.position[0])

    @property
    def y(self):
        return int(self.position[1])

    def set_x(self, x):
        self.position = (x, self.y)

    def set_y(self, y):
        self.position = (self.x, y)
