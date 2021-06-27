from math import sqrt


def distance(a, b):
    return sqrt((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2)

def length(points):
    previous_point = None
    total_length = 0
    for point in points:
        if previous_point is not None:
            total_length = total_length + distance(point, previous_point)
        previous_point = point
    return total_length


A = {'x': 0, 'y': 0}
B = {'x': 3, 'y': 8}
C = {'x': 12, 'y': -5}

ABC = length([A, B, C])
print(ABC)
