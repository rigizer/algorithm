import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    result = math.lcm(a, b)
    print(result)