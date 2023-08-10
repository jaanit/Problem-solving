import os
import math

n_cubes = int(input())
max = 0
# n_cubes = max * (max + 1) // 2
max = (-1 + math.sqrt(1 + 8 * n_cubes)) / 2
print(math.floor(max))