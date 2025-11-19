import sys
input = lambda: sys.stdin.readline().rstrip()

n, nlines = map(int, input().split())
start_time = [None] * (n + 1)
total = [0] * (n + 1)

for _ in range(nlines):
    c, keyword, hh, mm = input().split()
    c = int(c)
    hh = int(hh)
    mm = int(mm)
    current = hh * 60 + mm

    if keyword == 'START':
        start_time[c] = current
    else:
        total[c] += current - start_time[c]
        start_time[c] = None

for i in range(1, n + 1):
    hours = total[i] // 60
    minutes = total[i] % 60
    if i < n:
        print(hours, minutes)
    else:
        print(f'{hours} {minutes}')