s = input()
l = len(s)
x, y = 0, 0

for r in range(1, int(l / 2) + 1):
    for c in range(r, l + 1):
        if r * c == l:
            x, y = r, c

for i in range(x):
    for j in range(y):
        print(s[i + j * x], end='')