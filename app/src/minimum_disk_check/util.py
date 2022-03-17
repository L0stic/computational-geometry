from dataclasses import dataclass
import numpy as np
from .visual import plot_circle

TOLERANCE = 1e-14


def get_distance(p1: np.array, p2: np.array) -> float:
    diff = p1 - p2
    return np.sqrt((diff * diff).sum())


def get_s_2(a: float, b: float,  c: float) -> float:
    p = (a + b + c) / 2.0
    return p * (p - a) * (p - b) * (p - c)


@dataclass
class Disc:
    def __init__(self, center: np.array = None, radius: float = 0.0):
        self.center = center
        self.radius = radius

    def circumscribe_point(self, p: np.array):
        self.center = p
        self.radius = 0.0
        print(self.center, self.radius)

    def circumscribe_diameter(self, p1: np.array, p2: np.array):
        self.center = (p1 + p2) / 2.0
        self.radius = get_distance(p1, p2) / 2.0
        print(self.center, self.radius)

    def circumscribe_triangle(self, p1: np.array, p2: np.array, p3: np.array):
        a1 = get_distance(p2, p3)
        a2 = get_distance(p1, p3)
        a3 = get_distance(p1, p2)
        # print(a1, a2, a3)
        s_2 = get_s_2(a1, a2, a3)
        if s_2 < TOLERANCE:
            print("This is line")
            return False

        s = np.sqrt(s_2)

        k1 = (a1 * a1) * ((p1 - p2) * (p1 - p3)).sum()
        k2 = (a2 * a2) * ((p2 - p1) * (p2 - p3)).sum()
        k3 = (a3 * a3) * ((p3 - p1) * (p3 - p2)).sum()

        self.center = (k1 * p1 + k2 * p2 + k3 * p3) / (8 * s_2)
        self.radius = (a1 * a2 * a3) / (4.0 * s)
        print(self.center, self.radius)
        return True

    def is_contain(self, point: np.array) -> bool:
        distance = get_distance(self.center, point)
        diff = distance - self.radius
        if diff > TOLERANCE:
            return False
        else:
            return True

    def plot(self, figure=None, ax=None):
        if self.center is None:
            print("Empty set")
        elif len(self.center) == 2:
            plot_circle(self.center[0], self.center[1], self.radius, figure, ax)
        else:
            print("Unsupported dimension for visualisation")
