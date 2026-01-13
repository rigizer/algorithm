import sys
input = lambda: sys.stdin.readline().rstrip()

ml, mr, tl, tr = input().split()

def win(a, b):
    if a == b:
        return 0
    if (a == 'S' and b == 'P') or (a == 'R' and b == 'S') or (a == 'P' and b == 'R'):
        return 1
    return -1

ms_can = False
tk_can = False

ms_hands = [ml, mr]
tk_hands = [tl, tr]

for m in ms_hands:
    ok = True
    for t in tk_hands:
        if win(m, t) != 1:
            ok = False
            break
    if ok:
        ms_can = True

for t in tk_hands:
    ok = True
    for m in ms_hands:
        if win(t, m) != 1:
            ok = False
            break
    if ok:
        tk_can = True

if ms_can and not tk_can:
    print('MS')
elif tk_can and not ms_can:
    print('TK')
else:
    print('?')