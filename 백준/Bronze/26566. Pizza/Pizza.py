from math import pi

for _ in range(int(input())) :
    a, p1 = map(float, input().split())
    r, p2 = map(float, input().split())
    v1, v2 = a / p1, (pi * r**2) / p2
    print(['Slice of pizza', 'Whole pizza'][v1 < v2])