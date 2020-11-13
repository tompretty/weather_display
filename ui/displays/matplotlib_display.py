import matplotlib.pyplot as plt

from .base import Display


class MatplotlibDisplay(Display):
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw(self, window):
        self.ax.imshow(window.get_pil_image())
        plt.ion()
        plt.show()
        plt.pause(0.001)
