import sys
from apps import minimum_disk_check
from apps import polygon_monotonicity_check


import json
import os

visualisation = True
tolerance = 1e-9


def configure():
    path = os.path.abspath(os.path.dirname(__name__) + 'config.json')
    global tolerance, visualisation
    with open(path) as f:
        data = json.load(f)
        visualisation = bool(data["visualisation"])
        tolerance = float(data["tolerance"])
        f.close()


if __name__ == '__main__':
    problem = sys.argv[1]
    input_dir = sys.argv[2]
    output_dir = sys.argv[3]
    configure()

    print(f'start programme with\n -- input dir = "{input_dir}"\n -- output dir = "{output_dir}"')
    if problem == 'minimum_disk_check':
        minimum_disk_check(input_dir, output_dir, visualisation, tolerance)
    elif problem == 'polygon_monotonicity_check':
        polygon_monotonicity_check(input_dir, output_dir, visualisation)
    else:
        print('incorrect problem name')
