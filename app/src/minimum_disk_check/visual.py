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
