num = int(input())
seal = input()

b = 0
r = 0
o = 0
n = 0
z = 0
s = 0
i = 0
l = 0
v = 0
e = 0

for ch in seal:
    if ch == 'B':
        b += 1
    elif ch == 'R':
        r += 1
    elif ch == 'O':
        o += 1
    elif ch == 'N':
        n += 1
    elif ch == 'Z':
        z += 1
    elif ch == 'S':
        s += 1
    elif ch == 'I':
        i += 1
    elif ch == 'L':
        l += 1
    elif ch == 'V':
        v += 1
    elif ch == 'E':
        e += 1

e = e // 2
r = r // 2

print(min(b, r, o, n, z, s, i, l, v, e))