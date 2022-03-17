import sys
from apps import minimum_disk_check


if __name__ == '__main__':
    problem = sys.argv[1]
    input_dir = sys.argv[2]
    output_dir = sys.argv[3]
    visual = sys.argv[4] == 'True'

    print(f'start programme with\n -- input dir = "{input_dir}"\n -- output dir = "{output_dir}"\n -- visual mode = {visual}')
    if problem == 'minimum_disk_check':
        minimum_disk_check(input_dir, output_dir, visual)
    else:
        print('incorrect problem name')
