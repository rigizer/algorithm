l = int(input())
n = int(input())

want = []
max_if, max_real = 0, 0
idx_if, idx_real = 0, 0
for i in range(n):
    tmp = tuple(map(int,input().split()))
    if (tmp[1] - tmp[0] + 1) > max_if:
        max_if = tmp[1] - tmp[0] + 1
        idx_if = i + 1
    want.append(tmp)
print(idx_if)

cake = [True] * l
for idx, rnge in enumerate(want):
    chk = 0
    for i in range(rnge[0] - 1, rnge[1]):
        if cake[i]:
            cake[i] = False
            chk += 1
    if chk > max_real:
        max_real = chk
        idx_real = idx + 1
print(idx_real)