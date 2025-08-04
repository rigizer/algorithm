a, b = input().split()
result = []

for i in range(2, 37):
    try:
        x = int(a, i)
    except:
        continue
    for j in range(2, 37):
        if i == j:
            continue
        try:
            y = int(b, j)
        except:
            continue
        if x == y:
            result.append((x, i, j))

if len(result) == 0:
    print('Impossible')
elif len(result) == 1:
    print(result[0][0], result[0][1], result[0][2])
else:
    print('Multiple')