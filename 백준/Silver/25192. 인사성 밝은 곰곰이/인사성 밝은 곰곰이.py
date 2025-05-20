result = 0
data = set()
for _ in range(int(input())):
    s = input()
    if s == 'ENTER':
        data.clear()
        continue

    if s not in data:
        data.add(s)
        result += 1

print(result)