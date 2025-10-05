sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
px, py = map(int, input().split())

if sx == ex or sy == ey:
    result = 0
else:
    result = 1

if sy == ey and py == sy:
    if min(sx, ex) < px < max(sx, ex):
        if result == 0:
            result = 2
        else:
            result += 1

if sx == ex and px == sx:
    if min(sy, ey) < py < max(sy, ey):
        if result == 0:
            result = 2
        else:
            result += 1

print(result)