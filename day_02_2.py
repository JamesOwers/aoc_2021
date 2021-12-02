#!/usr/bin/env python
import sys

import numpy as np

def convert_to_aim_vector(input_line, aim):
    command, integer = input_line.split()
    integer = int(integer)
    if command == "forward":
        return (aim * integer, integer), aim
    elif command == "down":
        return (0, 0), aim + integer
    elif command == "up":
        return (0, 0), aim - integer
    else:
        raise ValueError(f"{command=} not expected")

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, "r") as fh:
        lines = fh.read().splitlines()
    curr_vector = np.array((0, 0))
    curr_aim = 0
    for line in lines:
        vector, curr_aim = convert_to_aim_vector(line, curr_aim)
        curr_vector += vector
    print(curr_vector.prod())
