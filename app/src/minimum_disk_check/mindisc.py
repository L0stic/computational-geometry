import random
import numpy as np
from .util import Disc


def find_min_disc(points):
    random.shuffle(points)
    disc = Disc()
    disc.circumscribe_diameter(np.array(points[0]), np.array(points[1]))
    for i in range(2, len(points)):
        if disc.is_contain(np.array(points[i])) < 0:
            disc = min_disc_with_point(list(points[0:i]), points[i])
    return disc


def min_disc_with_point(points, q):
    random.shuffle(points)
    disc = Disc()
    disc.circumscribe_diameter(np.array(points[0]), np.array(q))
    for i in range(1, len(points)):
        if disc.is_contain(np.array(points[i])) < 0:
            disc = min_disc_with_2_points(list(points[0:i]), points[i], q)
    return disc


def min_disc_with_2_points(points, q1, q2):
    disc = Disc()
    disc.circumscribe_diameter(np.array(q1), np.array(q2))
    for i in range(len(points)):
        if disc.is_contain(np.array(points[i])) < 0:
            disc.circumscribe_triangle(
                np.array(points[i]), np.array(q1), np.array(q2)
            )
    return disc


# def activate_min_disc(points, indexes):
#     return None
