import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    s = input().strip()
    if '.' in s:
        d, m, y = s.split('.')
    else:
        m, d, y = s.split('/')

    d = str(int(d)).zfill(2)
    m = str(int(m)).zfill(2)
    y = str(int(y)).zfill(4)

    print(f'{d}.{m}.{y} {m}/{d}/{y}')