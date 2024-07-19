a, b = map(int, input().split())
data = []
for i in range(-1000, 10001):
    if i * (2 * a - i) == b:
        data = list(set([-i, -(2 * a - i)]))
print(*sorted(data))