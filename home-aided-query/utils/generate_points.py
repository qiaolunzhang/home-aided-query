 # -*- coding: utf-8 -*-
import math
import random
import struct


def generate_points(x, y, R):
    point_random = R + random.random()
    theta = 2.0 * math.pi * random.random()
    x1 = x + R * math.sin(theta)
    y1 = y + R * math.cos(theta)
    if x1 < 0:
        x1 = -x1
    if y1 < 0:
        y1 = -y1
    x1 = str(x1)
    y1 = str(y1)
    point = x1 + " " + y1
    with open("./points.txt", 'a+') as f:
        f.write(point)
        f.write('\n')

for i in range(10):
    for i in range(1, 11):
        generate_points(5, 5, i)

for i in range(100):
    for i in range(11, 20):
        generate_points(5, 5, i)
