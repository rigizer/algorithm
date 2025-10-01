a, b, c = map(int, input().split())

if c == 0:
    result = int((a + b) ** 0.5)
elif a == 0:
    result = c ** 2 - b
else:
    result = c ** 2 - a

print(result)