# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 02:52:24 2020
Name of file: linear_sensor_to_steering_angle.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation
"""
import numpy as np
import math
import os
import sys
import argparse

r = 5  # Radius of the circle created by the rotation of the wheel.
# 'a' and 'b' represent the 'x' and 'y' offset(translation) of the circle.
a = -7
b = 8
piston_fixed_part = 5
min_inches = 0
max_inches = 4

def compute_angle(n = 4):
    if min_inches > n or n > max_inches:
        raise ValueError('Piston inches value out of range!')

    d = n + piston_fixed_part  # Total distance of the piston.
    dot_product_a_b = a ^ 2 + b ^ 2
    Q = dot_product_a_b - d ^ 2 + r ^ 2
    translation_length = math.sqrt(dot_product_a_b)
    R = Q / translation_length
    Beta = math.atan2(b / a)
    Theta = Beta - math.asin(R)

    return Theta

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

    # Note: In the drawings, the variable 'x' is used to represent the length in inches of the movable part of the sensor. Here 'n' is used instead.
    n = args[1]
    # print(f'length of {n} is {compute_angle(n)} radians')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))