import numpy as np
from numpy import genfromtxt
import math


def analyze_direction(log_location):
    DIRECTION = [1, 2, 3]
    DIRECTION_WITH_TIME = [0, 4, 5, 6]

    direction_logs = genfromtxt(log_location, delimiter=',')
    directions_with_time = direction_logs[:, DIRECTION_WITH_TIME]

    mean_direction = np.mean(directions_with_time[:, DIRECTION], axis=0)

    mean_angle = 0
    std_angle = 0

    for (time, x, y, z) in directions_with_time:
        direction = np.array([x, y, z])

        angle = math.atan2(
            np.linalg.norm(np.cross(direction, mean_direction)),
            np.dot(direction, mean_direction))

        mean_angle += angle
        std_angle += angle ** 2

    mean_angle /= len(directions_with_time)
    std_angle = (std_angle / len(directions_with_time) - mean_angle ** 2) ** 0.5

    print(mean_angle, std_angle)
