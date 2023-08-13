data = set()
result = 0
for _ in range(5):
    s = int(input())
    if s in data:
        result -= s
        data.discard(s)
    else:
        data.add(s)
        result += s
print(result)