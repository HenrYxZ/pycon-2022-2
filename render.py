import numpy as np
from progress.bar import Bar


from camera import Camera
from constants import *
from raytracer import Raytracer
from scene import Scene
import utils


def render(scene: Scene, camera: Camera, width: int, height: int) -> np.ndarray:
    arr = np.zeros([height, width, COLOR_CHANNELS], dtype=np.uint8)
    raytracer = Raytracer(height, width, scene, camera)
    bar = Bar(
        'Raytracing',
        max=height,
        suffix='%(percent)d%% [%(elapsed_td)s / %(eta_td)s]',
        check_tty=False
    )
    for j in range(height):
        for i in range(width):
            color = raytracer.compute_color(j, i)
            arr[j][i] = utils.convert_to_rgb(color)
        # show progress for a completed row
        bar.next()
    bar.finish()
    return arr
