import sys
import math
input = lambda: sys.stdin.readline().rstrip()

w = int(input())
x = math.sqrt(w // 2)
print(int(x) * 8)