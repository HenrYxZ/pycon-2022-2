from dataclasses import dataclass
import numpy as np


class Scene:
    def __init__(self):
        self.objects = []


@dataclass
class Sphere:
    pos: np.ndarray
    r: float
    color: np.ndarray

    def normal_at(self, p: np.ndarray):
        # TODO: implement calculation of normal
        pass
