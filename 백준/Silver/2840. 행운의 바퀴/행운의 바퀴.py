import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

D = []
cum = 0
obs = []
for _ in range(K):
    parts = input().split()
    s = int(parts[0])
    c = parts[1]
    d = s % N
    cum = (cum + d) % N
    D.append(cum)
    obs.append((c, cum))

Dk = D[-1]

wheel = ['?'] * N
letter_pos = dict()
conflict = False

for c, Di in obs:
    pos = (Dk - Di) % N
    if wheel[pos] == '?':
        if c in letter_pos and letter_pos[c] != pos:
            conflict = True
            break
        wheel[pos] = c
        letter_pos[c] = pos
    else:
        if wheel[pos] != c:
            conflict = True
            break

if conflict:
    print('!')
else:
    print(''.join(wheel))