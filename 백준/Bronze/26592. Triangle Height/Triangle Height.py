import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = []

for _ in range(n):
    area, base = map(float, input().split())
    height = (2 * area) / base
    result.append(f'The height of the triangle is {height:.2f} units')

for line in result:
    print(line)