from dataclasses import dataclass
import numpy as np


import utils


@dataclass
class DirectionalLight:
    direction: np.ndarray

    def get_l(self):
        return -self.direction


class Scene:
    def __init__(self):
        self.objects = []
        self.light = DirectionalLight(
            utils.normalize(np.array([0.3, -1.0, 0.5]))
        )

@dataclass
class Sphere:
    pos: np.ndarray
    r: float
    color: np.ndarray

    def normal_at(self, p: np.ndarray):
        n = utils.normalize(p - self.pos)
        return n
