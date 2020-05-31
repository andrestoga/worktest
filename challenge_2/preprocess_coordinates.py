# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 05:52:24 2020
Name of file: preprocess_coordinates.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation. Challenge number 2
"""
from math import *
import numpy as np
from matplotlib import pyplot as plt
import random
from scipy.signal import savgol_filter
import sys
import pandas as pd
import json

coord_noise = 0.5


def points_in_circum(r, n=100, add_noise=1):
    if add_noise:
        return np.array(
            [(random.gauss(cos(2 * pi / n * x) * r, coord_noise), \
              random.gauss(sin(2 * pi / n * x) * r,
             coord_noise))for x in range(0, n + 1)])
    else:
        return np.array([(cos(2 * pi / n * x) * r, sin(2 * pi / n * x) * r) \
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
    # TODO: Parse the boundary from the provided region.kml KML file and generate a new KML file with the updated boundary.
    else:
        df1 = pd.read_json(path)
        df1[['coord_x', 'coord_y']] = pd.DataFrame(df1.coordinates.tolist(), index=df1.index)
        df = pd.DataFrame(df1['coordinates'].to_list(), columns=['coord_x', 'coord_y'])

        n = df.to_numpy()

        x = n[:, 0]
        y = n[:, 1]

    # TODO: Remove outliers before applying the filter.
    # TODO: Test with other filters.
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
