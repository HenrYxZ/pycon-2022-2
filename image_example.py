import numpy as np
from PIL import Image


WIDTH = 288
HEIGHT = 192
COLOR_CHANNELS = 3


def main():
    arr = np.zeros([HEIGHT, WIDTH, COLOR_CHANNELS], dtype=np.uint8)
    img = Image.fromarray(arr)
    img.save("output.png")


if __name__ == '__main__':
    main()
