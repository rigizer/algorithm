import os
from collections import deque
input = lambda: os.sys.stdin.readline().rstrip()

n, p = map(int, input().split())
note = [list(map(int, input().split())) for _ in range(n)]

frets = [deque([0]) for _ in range(p + 1)]
max_fret = [0] * (p + 1)

result = 0

for line, fret in note:
    while frets[line]:
        if max_fret[line] > fret:
            frets[line].pop()
            max_fret[line] = frets[line][-1] if frets[line] else 0
            result += 1
    
        elif max_fret[line] < fret:
            frets[line].append(fret)
            max_fret[line] = fret
            result += 1
            break

        elif max_fret[line] == fret:
            break

print(result)