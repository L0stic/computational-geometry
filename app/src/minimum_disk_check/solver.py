import numpy as np
from .util import Disc
from .mindisc import find_min_disc


def read_data(file_path_points: str, file_path_indexes: str) -> (list, list):
    points: list = []
    with open(file_path_points) as file:
        for line in file.readlines():
            if line.startswith('#'):
                continue
            tmp = line.split(' ')
            if len(tmp) > 0:
                points.append(list(map(float, tmp)))
            else:
                points.append(list())
        file.close()

    indexes: list = []
    with open(file_path_indexes) as file:
        for line in file.readlines():
            if line.startswith('#'):
                continue
            if line.startswith('empty'):
                indexes.append(list())
                continue
            tmp = line.split(' ')
            if len(tmp) > 0:
                indexes.append(list(map(int, tmp)))
        file.close()

    return points, indexes


def solve(points, indexes):
    result = []
    min_disc = None
    for j in range(len(indexes)):
        if len(indexes[j]) == 0:
            print("empty set")

            if len(points) == 0:
                result.append(True)
                if min_disc is None:
                    min_disc = Disc()
                    print("min_disc:", min_disc.to_string())
            else:
                result.append(False)
            continue
        elif len(indexes[j]) == 1:
            print("one set")

            if len(points) == 1:
                result.append(True)
                if min_disc is None:
                    min_disc = Disc()
                    min_disc.circumscribe_point(
                        np.array(points[indexes[j]][0])
                    )
                    print("min_disc:", min_disc.to_string())
            else:
                result.append(False)
            continue

        if min_disc is None:
            print("find min_disc")
            min_disc = find_min_disc(list(points))
            print("min_disc:", min_disc.to_string())

        disc = Disc()
        start_points = [points[i] for i in indexes[j]]

        if len(indexes[j]) == 2:
            print("two points")
            disc.circumscribe_diameter(
                np.array(start_points[0]), np.array(start_points[1])
            )
        elif len(indexes[j]) == 3:
            print("three points")
            if not disc.circumscribe_triangle(
                np.array(start_points[0]), np.array(start_points[1]), np.array(start_points[2])
            ):
                result.append(False)
                continue
        else:
            print("Error: wrong indexes")
            return None, None

        if not min_disc.is_equal(disc):
            result.append(False)
        else:
            result.append(True)
    return result, min_disc
