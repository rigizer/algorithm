n, x = map(int, input().split())

result = -1
for _ in range(n):
    s, t = map(int, input().split())

    if result < s and s + t <= x:
        result = s

print(result)