from math import pi


def f(radius):
    return 2 * pi * radius, pi * radius ** 2


print('result', f(int(input('write the length of the radius\n'))))
