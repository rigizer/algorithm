t = int(input())
for _ in range(t):
    d = [0] * 27
    v = input()
    for i in range(len(v)):
        d[int(ord(v[i]))-65] += 1

    r = 0
    for i in range(26):
        if d[i] == 0:
            r += i + 65

    print(r)