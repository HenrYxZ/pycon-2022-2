import numpy as np

from camera import Camera
from constants import *
from scene import Scene, Sphere
import utils


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

    def at(self, t: float):
        return self.pr + t * self.nr


class Raytracer:
    def __init__(self, height: int, width: int, scene: Scene, camera: Camera):
        self.height = height
        self.width = width
        self.scene = scene
        self.camera = camera

    def compute_color(self, j: float, i: float) -> np.ndarray:
        # create ray for pixel
        pp = self.camera.project_pixel(j, i, self.width, self.height)
        nr = utils.normalize(pp - self.camera.pos)
        ray = Ray(self.camera.pos, nr)
        # intersect ray with all objects
        min_t = float('inf')
        min_obj = None
        for obj in self.scene.objects:
            t = ray.intersect(obj)
            if 0 < t < min_t:
                min_t = t
                min_obj = obj
        # calculate color for hit point
        if isinstance(min_obj, Sphere):
            n = min_obj.normal_at(ray.at(min_t))
            l = self.scene.light.get_l()
            n_dot_l = np.clip(np.dot(n, l), 0, 1)
            ambient = 0.2
            color = (n_dot_l + ambient) * min_obj.color
        else:
            color = np.zeros(COLOR_CHANNELS)
        return color
