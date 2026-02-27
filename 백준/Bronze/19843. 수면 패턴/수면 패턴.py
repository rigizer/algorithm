import sys
input = lambda: sys.stdin.readline().rstrip()

day_to_idx = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4
}

T, N = map(int, input().split())

total_sleep = 0
for _ in range(N):
    d1, h1, d2, h2 = input().split()
    h1 = int(h1)
    h2 = int(h2)

    start = day_to_idx[d1] * 24 + h1
    end = day_to_idx[d2] * 24 + h2
    total_sleep += (end - start)

need = T - total_sleep

if need <= 0:
    print(0)
elif need > 48:
    print(-1)
else:
    print(need)