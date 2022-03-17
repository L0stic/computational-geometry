from matplotlib import pyplot as plt
from src.minimum_disk_check.visual import plot_points
from src.minimum_disk_check.solver import solve, read_data

import time


def minimum_disk_check(input_dir, output_dir, visual):
    points, indexes = read_data(input_dir + "/input_points.txt", input_dir + "/input_indexes.txt")

    start = time.time() * 1000
    print("points:", points)
    print("indexes:", indexes)
    result, min_disc = solve(points, indexes)
    end = time.time() * 1000
    print(f"total time for solving: {int(end - start)} ms")

    if result is None:
        return

    print("result:", result)

    if visual:
        figure, axes = plt.subplots()
        plot_points(points, figure=figure, ax=axes)
        plot_points([points[i] for i in indexes[-1]], 'r', '*', figure, axes)
        if min_disc is not None:
            min_disc.plot(figure, axes)
        path = output_dir + '/mindisc_visual.png'
        plt.grid()
        plt.savefig(path)
        print(f'algorithm result visualization saved to "{path}"')

    path = output_dir + '/output.txt'

    with open(path, "w") as file:
        for i in range(len(indexes)):
            file.write(f"{indexes[i]} - {result[i]}\n")
        file.close()
    print(f'algorithm result saved to "{path}"')


if __name__ == '__main__':
    minimum_disk_check('./res/mindisc', './res/mindisc', True)
