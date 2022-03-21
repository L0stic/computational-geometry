import numpy as np
from .util import sign, triangle_area, is_clockwise_polygon, turn_around_polygon


def read_data(file_path_vertexes: str, file_path_direction: str) -> (list, list, bool):
    vertexes = []
    with open(file_path_vertexes) as file:
        for line in file.readlines():
            if line.startswith('#'):
                continue
            vertexes.append(list(map(int, line.split(' '))))
        file.close()

    direction: list = []
    with open(file_path_direction) as file:
        for line in file.readlines():
            if line.startswith('#'):
                continue
            direction = list(map(int, line.split(' ')))
        file.close()

    vertexes = np.array(vertexes, dtype=int)

    is_clockwise = is_clockwise_polygon(polygon=vertexes)

    if not is_clockwise:
        vertexes = turn_around_polygon(polygon=vertexes)
        print("counterclockwise polygon, fixed")
    print(f"polygon size: {len(vertexes)}")
    return list(vertexes.tolist()), direction, is_clockwise


def solve(polynom, direction):
    ortho_dir = -direction[1], direction[0]
    poly_size = len(polynom)

    target_vertex_id = -1 % poly_size
    support_vertex_id = (-1 + 1) % poly_size
    v1 = polynom[target_vertex_id]
    v2 = polynom[support_vertex_id]
    v3 = polynom[target_vertex_id][0] + ortho_dir[0], polynom[target_vertex_id][1] + ortho_dir[1]
    edge1 = v2[0] - v1[0], v2[1] - v1[1]
    edge2 = v3[0] - v1[0], v3[1] - v1[1]
    last_sgn = sign(triangle_area(edge1, edge2))

    changing_sng = 0

    for i in range(poly_size):
        target_vertex_id = i % poly_size
        support_vertex_id = (i + 1) % poly_size
        v1 = polynom[target_vertex_id]
        v2 = polynom[support_vertex_id]
        v3 = polynom[target_vertex_id][0] + ortho_dir[0], polynom[target_vertex_id][1] + ortho_dir[1]

        edge1 = v2[0] - v1[0], v2[1] - v1[1]
        edge2 = v3[0] - v1[0], v3[1] - v1[1]

        current_sng = sign(triangle_area(edge1, edge2))
        if current_sng == 0:
            continue
        if current_sng + last_sgn == 0:
            changing_sng += 1
        last_sgn = current_sng

    return changing_sng == 2
