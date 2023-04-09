import math

n = int(input())
for i in range(1, 10_001):
    if i > math.sqrt(n):
        break

print("The largest square has side length {}.".format(i - 1))