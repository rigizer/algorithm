w, h = map(int, input().split())
result = w + h - (w ** 2 + h ** 2) ** 0.5
print(result)