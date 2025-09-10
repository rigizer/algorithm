import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
potions = list(map(int, input().split()))

v = 0.0
result = []
for a in potions:
    v = 1 - (1 - v) * (1 - a / 100)
    result.append(f'{v * 100:.6f}')

print('\n'.join(result))