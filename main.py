import numpy as np
from PIL import Image


from constants import *
from camera import Camera
from render import render
from scene import Scene, Sphere


rng = np.random.default_rng()
COLORS = [
    rng.random(COLOR_CHANNELS),
    rng.random(COLOR_CHANNELS),
    rng.random(COLOR_CHANNELS)
]
RS = [0.5, 0.2, 0.3]
POS = [
    np.array([0.0, 0.0, 3.0]),
    np.array([-0.3, 0.0, 2.0]),
    np.array([1.2, 0.0, 1.7])
]

WIDTH = 288
HEIGHT = 192


def main():
    # Create a Camera
    v_view = np.array([0.0, 0.0, 1.0])
    v_up = np.array([0.0, 1.0, 0.0])
    sx = 35
    sy = 24
    d = 26
    camera = Camera(v_view, v_up, sx, sy, d)

    # Create a Scene
    scene = Scene()
    for i in range(len(COLORS)):
        scene.objects.append(Sphere(POS[i], RS[i], COLORS[i]))

    # Render an image
    im_arr = render(scene, camera, WIDTH, HEIGHT)
    img = Image.fromarray(im_arr)
    img.save("output.png")


if __name__ == '__main__':
    main()
