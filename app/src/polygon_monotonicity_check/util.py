import numpy as np


def turn_around_polygon(polygon: np.array):
    return np.flip(polygon, 0)


def is_clockwise_polygon(polygon: np.array) -> bool:
    for i in range(len(polygon)):
        edge1 = np.concatenate((polygon[i+1] - polygon[i], [0]))
        edge2 = np.concatenate((polygon[i+2] - polygon[i+1], [0]))
        if np.cross(edge1, edge2)[2] == 0:
            continue
        return np.cross(edge1, edge2)[2] < 0


def sign(a):
    return 1 if a > 0 else -1 if a < 0 else 0


def triangle_area(edge1, edge2):
    return edge1[0] * edge2[1] - edge1[1] * edge2[0]
