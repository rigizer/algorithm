import sys
input = lambda: sys.stdin.readline().rstrip()

pos = {
    '1': (0,0), '2': (1,0), '3': (2,0),
    '4': (0,1), '5': (1,1), '6': (2,1),
    '7': (0,2), '8': (1,2), '9': (2,2),
    '0': (1,3)
}

def effort(a, b):
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    return abs(x1 - x2) + abs(y1 - y2)

hh, mm = input().split(':')
hh = int(hh)
mm = int(mm)

candidates = []

for h in range(100):
    for m in range(100):
        if h % 24 == hh and m % 60 == mm:
            hstr = str(h).zfill(2)
            mstr = str(m).zfill(2)
            s = hstr + mstr
            cost = effort(s[0], s[1]) + effort(s[1], s[2]) + effort(s[2], s[3])
            candidates.append((cost, hstr + ':' + mstr))

candidates.sort()
result = candidates[0][1]
print(result)