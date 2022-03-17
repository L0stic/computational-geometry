# Computational geometry

Solved problems:
- minimum_disk_check 

## Install and Build
```shell
pip install -r requirements.txt
```

## MinDisc
```shell
cd app
python manage.py minimum_disk_check ./res/mindisc ./res/mindisc True
```

Example:
- `input_points.txt`
  ```txt
  1.0 5.0
  2.0 3.0
  3.0 2.0
  3.0 4.0
  ```
- `input_indexes.txt`
  ```txt
  # comment
  empty
  0
  0 1
  0 1 2
  ```
- `output.txt` - result for every indexes
  ```txt
  [] - False
  [0] - False
  [0, 1] - True
  [0, 1, 2] - True
  ```
- `mindisc_visual.png` - visualisation of last indexes
