import numpy as np


import utils


class Camera:
    def __init__(
        self, pos: np.ndarray, v_view: np.ndarray, v_up: np.ndarray,
        sx: float, sy: float, d: float
    ):
        self.pos = pos
        self.sx = sx
        self.sy = sy
        self.d = d
        self.n2 = utils.normalize(v_view)
        self.n0 = utils.normalize(np.cross(v_up, v_view))
        self.n1 = utils.normalize(np.cross(self.n2, self.n0))
        pc = self.pos + d * self.n2
        self.p00 = pc - (sx / 2) * self.n0 - (sy / 2) * self.n1

    def project_pixel(self, j: float, i: float, width: int, height: int):
        xp = ((i + 0.5) / width) * self.sx
        yp = ((height - (j + 0.5)) / height) * self.sy
        pp = self.p00 + xp * self.n0 + yp * self.n1
        return pp
