import numpy as np


from constants import *


def normalize(arr: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(arr)
    if norm == 0:
        return arr
    return arr / norm


def convert_to_rgb(color: np.ndarray) -> np.ndarray:
    color = color * MAX_COLOR_VALUE
    rgb_color = color.round().astype(np.uint8)
    return rgb_color
