import numpy as np
from .util import Disc


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
            print("zero way")
            if len(points) == 0:
                result.append(True)
                if min_disc is None:
                    min_disc = Disc()
            result.append(False)
            continue

        start_points = []
        other_points = []
        for i in range(len(points)):
            if i in indexes[j]:
                start_points.append(points[i])
            else:
                other_points.append(points[i])

        disc = Disc()

        if len(indexes[j]) == 1:
            print("one way")
            disc.circumscribe_point(np.array(start_points[0]))

        elif len(indexes[j]) == 2:
            print("two way")
            disc.circumscribe_diameter(np.array(start_points[0]), np.array(start_points[1]))
            for other_point in other_points:
                other_point = np.array(other_point)
                if not disc.is_contain(other_point):
                    disc.circumscribe_triangle(
                        np.array(start_points[0]), np.array(start_points[1]), other_point
                    )

        elif len(indexes[j]) == 3:
            print("three way")
            if not disc.circumscribe_triangle(
                    np.array(start_points[0]), np.array(start_points[1]), np.array(start_points[2])
            ):
                result.append(False)
                continue

        else:
            print("Error")
            return None

        while len(other_points) > 0:
            other_point = np.array(other_points.pop())
            if not disc.is_contain(other_point):
                result.append(False)
                break

        if len(result) == j:
            result.append(True)

            if min_disc is None:
                min_disc = disc
    return result, min_disc
