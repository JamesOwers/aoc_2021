#!/usr/bin/env python
import sys

import numpy as np

def convert_to_depth_vector(input_line):
    command, integer = input_line.split()
    integer = int(integer)
    if command == "forward":
        return (0, integer)
    elif command == "backward":
        return (0, -integer)
    elif command == "down":
        return (integer, 0)
    elif command == "up":
        return (-integer, 0)
    else:
        raise ValueError(f"{command=} not expected")

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, "r") as fh:
        lines = fh.read().splitlines()
    vectors = np.array([convert_to_depth_vector(line) for line in lines])
    print(vectors.sum(axis=0).prod())
