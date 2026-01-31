import sys
input = lambda: sys.stdin.readline().rstrip()

def precompute(limit=1000):
    sol = [None] * (limit + 1)
    sol[1] = (0, 0, 0)
    for a in range(0, limit):
        if 1 + a > limit:
            break
        for b in range(0, limit + 1):
            base = 1 + a + b * (a + 1)
            if base > limit:
                break
            step = a + b + 1
            max_c = (limit - base) // step
            for c in range(0, max_c + 1):
                r = base + c * step
                lines = a + b + c
                cur = sol[r]
                if cur is None or lines < (cur[0] + cur[1] + cur[2]):
                    sol[r] = (a, b, c)
    return sol

data = sys.stdin.read().split()
t = int(data[0])
ns = list(map(int, data[1:1 + t]))

sol = precompute(1000)

result = []
for n in ns:
    a, b, c = sol[n]
    lines = []
    for i in range(1, a + 1):
        lines.append((0, i))
    for j in range(1, b + 1):
        lines.append((1, 100 + j))
    for k in range(0, c):
        lines.append((-1, 3000 + k))
    result.append(str(len(lines)))
    for m, bb in lines:
        result.append(f'{m} {bb}')

for i, line in enumerate(result):
    if i + 1 == len(result):
        print(line, end='')
    else:
        print(line)