# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 02:52:24 2020
Name of file: linear_sensor_to_steering_angle.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation. Challenge number 1
"""
import numpy as np
import math
import sys

r = 5  # Radius of the circle created by the rotation of the wheel.
# 'a' and 'b' represent the 'x' and 'y' offset(translation) of the circle.
a = -7
b = 8
piston_fixed_part = 5
min_inches = 0.7
max_inches = 10
init_state = 1.436

# Note: In the drawings, the variable 'x' is used to represent the length in inches of the movable part of
# the sensor. Here 'n' is used instead.
def compute_angle(n):
    if min_inches > n or n > max_inches:
        raise ValueError(f'Error. Piston value should be between {min_inches} and {max_inches}')

    d = n + piston_fixed_part  # Total distance of the piston.
    dot_product_a_b = a**2 + b**2
    Q = (dot_product_a_b - d**2 + r**2) / (2 * r) # See written notes
    print(f"Q {Q}")
    translation_length = math.sqrt(dot_product_a_b)
    print(f"Translation {translation_length}")
    R = Q / translation_length # See written notes
    print(f"R {R}")
    # beta = math.atan2(b, abs(a))
    beta = math.atan2(b, a)
    print(f"B {beta}")
    theta = beta - math.asin(R)

    # TODO: Check that the range is between 45 to -45
    return round(theta - init_state, 3)


def main(args):
    if 2 > len(args) > 0:
        x = float(args[0])
        print(f'Length of {x} is {compute_angle(x)} radians')
    else:
        print("Error. You must pass at least one float argument")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))