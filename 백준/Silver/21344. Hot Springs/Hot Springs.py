import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t = list(map(int, input().split()))
t.sort()

m = (n - 1) // 2
result = [t[m]]
l = m - 1
r = m + 1
go_right = True

while l >= 0 or r < n:
    if go_right:
        if r < n:
            result.append(t[r])
            r += 1
        elif l >= 0:
            result.append(t[l])
            l -= 1
    else:
        if l >= 0:
            result.append(t[l])
            l -= 1
        elif r < n:
            result.append(t[r])
            r += 1
    go_right = not go_right

print(' '.join(map(str, result)))