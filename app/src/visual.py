import numpy as np
from matplotlib import pyplot as plt


def plot_circle(x, y, r, figure=None, ax=None):
    if ax is None:
        ax = plt.gca()

    if figure is None:
        figure = plt.gcf()

    draw_circle = plt.Circle((x, y), r, fill=False)
    plt.gcf().gca().add_artist(draw_circle)
    ax.plot(x, y, 'o', color='y')


def plot_points(points, c='b', m='.', figure=None, ax=None):
    if ax is None:
        ax = plt.gca()

    if figure is None:
        figure = plt.gcf()

    plt.scatter([p[0] for p in points], [[p[1] for p in points]], c=c, marker=m)


def plot_vector(vector: np.array, start_point: np.array = None, scale=1, c='b', m='.', figure=None, ax=None):
    if ax is None:
        ax = plt.gca()

    if figure is None:
        figure = plt.gcf()

    if start_point is None:
        start_point = np.zeros(len(vector))
    finish_point = start_point + scale * vector

    plt.plot([start_point[0], finish_point[0]], [start_point[1], finish_point[1]])


def plot_polygon(vertexes: np.array, figure=None, ax=None):
    if ax is None:
        ax = plt.gca()

    if figure is None:
        figure = plt.gcf()

    vertexes = np.append(vertexes, [vertexes[0]], axis=0)
    plt.plot(vertexes[:, 0], vertexes[:, 1])
