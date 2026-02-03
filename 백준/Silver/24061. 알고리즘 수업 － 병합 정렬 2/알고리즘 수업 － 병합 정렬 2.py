import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(1_000_000)

n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0] * n
cnt = 0

def merge(p, q, r):
    global cnt
    i, j, t = p, q + 1, p
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            i += 1
        else:
            tmp[t] = a[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = a[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = a[j]
        j += 1
        t += 1

    for idx in range(p, r + 1):
        a[idx] = tmp[idx]
        cnt += 1
        if cnt == k:
            print(*a)
            sys.exit(0)

def merge_sort(p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(p, q)
    merge_sort(q + 1, r)
    merge(p, q, r)

merge_sort(0, n - 1)
print(-1)