import matplotlib.pyplot as plt
from PIL import Image

from .base import Display


class MatplotlibDisplay(Display):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.fig, self.ax = plt.subplots()

    def draw(self):
        image = Image.open(self.image_path)
        self.ax.imshow(image)
        plt.ion()
        plt.show()
        plt.pause(0.001)
