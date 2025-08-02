n, m, a, k = map(int, input().split())
t = (a - k)
if t / n >= 1:
    maxs = n
else:
    maxs = t + 1
if float(int(t / m)) == t / m:
    mins = int(t / m) + 1
else:
    mins = int(t / m) + 2
print(maxs, mins)