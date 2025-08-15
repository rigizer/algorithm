n, h = map(int, input().split())
d = list(map(int, input().split()))

result = 0
for i in d:
    h -= i
    result += 1
    if h <= 0:
        break
print(-1 if h > 0 else result)