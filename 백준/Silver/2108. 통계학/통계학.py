def round(n):
    return int(n + 0.5) if n >= 0 else int(n - 0.5)

n = int(input())
ns = sorted([int(input()) for _ in range(n)])

print(round(sum(ns) / n))
print(ns[n // 2])

data = {}
for i in ns:
    if i not in data:
        data[i] = 1
    else:
        data[i] += 1

max_freq = max(data.values())
modes = [k for k, v in data.items() if v == max_freq]
modes.sort()

if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

print(ns[-1] - ns[0])