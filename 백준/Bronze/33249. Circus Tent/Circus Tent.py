import sys
input = lambda: sys.stdin.readline().rstrip()

import math

d, h = map(float, input().split())
R = (d + 10.0) / 2.0
area = 2.0 * math.pi * R * h + math.pi * R * R
sys.stdout.write(f"{area:.15f}")