from math import sqrt

A = {'x': 0, 'y': 0}
B = {'x': 3, 'y': 8}
C = {'x': 12, 'y': -5}

AB = sqrt((A['x'] - B['x']) ** 2 + (A['y'] - B['y']) ** 2)
BC = sqrt((C['x'] - B['x']) ** 2 + (C['y'] - B['y']) ** 2)

ABC = AB + BC
print(ABC)
