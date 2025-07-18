n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    dist = (abs(x) + abs(y) + abs(-x - y)) // 2
    print(dist)