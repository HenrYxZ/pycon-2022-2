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
RS = [0.8, 0.2, 0.3]
POS = [
    np.array([0.0, 0.0, 3.0]),
    np.array([-0.3, -0.05, 2.0]),
    np.array([0.55, 0.2, 1.7])
]

SCREEN_SCALE = 3
WIDTH = 288 * SCREEN_SCALE
HEIGHT = 192 * SCREEN_SCALE


def main():
    # Create a Camera
    cam_pos = np.array([0.0, 0.0, 0.0])
    v_view = np.array([0.0, 0.0, 1.0])
    v_up = np.array([0.0, 1.0, 0.0])
    sx = 35
    sy = 24
    d = 26
    camera = Camera(cam_pos, v_view, v_up, sx, sy, d)

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
