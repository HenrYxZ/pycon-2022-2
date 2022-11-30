import numpy as np

from camera import Camera
from constants import *
from scene import Scene, Sphere


class Ray:
    def __init__(self, pr: np.ndarray, nr: np.ndarray):
        self.pr = pr
        self.nr = nr

    def intersect_sphere(self, obj: Sphere) -> float:
        diff = self.pr - obj.pos
        b = np.dot(self.nr, diff)
        c = np.dot(diff, diff) - obj.r ** 2
        discriminant = b ** 2 - c
        if b > 0 or discriminant < 0:
            return -1
        t = -b - np.sqrt(discriminant)
        return t

    def intersect(self, obj) -> float:
        if isinstance(obj, Sphere):
            t = self.intersect_sphere(obj)
        else:
            raise Exception(
                f"{type(obj)} object type doesn't implement intersect function"
            )
        return t


class Raytracer:
    def __init__(self, height: int, width: int, scene: Scene, camera: Camera):
        self.height = height
        self.width = width
        self.scene = scene
        self.camera = camera

    def compute_color(self, j: float, i: float) -> np.ndarray:
        # TODO: implement color calculation
        color = np.ones(COLOR_CHANNELS)
        return color
