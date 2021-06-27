from math import sqrt


def distance(a, b):
    return sqrt((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2)


A = {'x': 0, 'y': 0}
B = {'x': 3, 'y': 8}
C = {'x': 12, 'y': -5}

AB = distance(A, B)
BC = distance(B, C)

ABC = AB + BC
print(ABC)
