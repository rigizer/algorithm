n, h, v = map(int, input().split())
result = max(h, n - h) * max(v, n - v)
print(result * 4)