from math import *
import numpy as np
from matplotlib import pyplot as plt
import random
from scipy.signal import savgol_filter
import sys

coord_noise = 0.5


def points_in_circum(r, n=100, add_noise=1):

    if add_noise:
        return np.array(
            [(random.gauss(cos(2 * pi / n * x) * r, coord_noise),
              random.gauss(sin(2 * pi / n * x) * r, coord_noise)) \
             for x in range(0, n + 1)])

    return np.array(
        [(cos(2 * pi / n * x) * r, sin(2 * pi / n * x) * r) \
         for x in range(0, n + 1)])

def compute_filter(path=""):

  if not path:
    n_points = 100
    radius = 10
    coordinates = points_in_circum(radius, n_points, add_noise=1)

    x = coordinates[:, 0]
    y = coordinates[:, 1]

    num_outliers = 3
    offset = 3
    outliers = np.empty((0, 2), float)

    for i in range(num_outliers):
        rnd_pnt = random.randint(0, n_points)
        m = y[rnd_pnt] / x[rnd_pnt]
        x[rnd_pnt] = x[rnd_pnt] + (offset if x[rnd_pnt] > 0 else -offset)
        y[rnd_pnt] = m * x[rnd_pnt]
        outliers = np.append(outliers, np.array([[x[rnd_pnt], y[rnd_pnt]]]), axis=0)
  else:
    # TODO: Get the points from the .json file and dump them in the x and y variables.
    x = []
    y = []

  yhat = savgol_filter(y, 19, 3)

  if not path:
    xtmp = outliers[:, 0]
    ytmp = outliers[:, 1]
    plt.plot(xtmp, ytmp, 'yo')

  plt.plot(x, y)
  plt.plot(x, yhat, color='red')
  plt.show()

def main(args):
    if 2 > len(args) > 0:
        file_path = args[0]
        compute_filter(file_path)
    else:
        compute_filter()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))