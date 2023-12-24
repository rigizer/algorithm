t = dict()
for _ in range(int(input())):
    i, j = map(str, input().split())
    t[i] = j
result = 0
for i, j in t.items():
    if int(j) > int(t['jinju']):
        result += 1
print(t['jinju'])
print(result)