import math

def distance (location1, location2):
    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))
