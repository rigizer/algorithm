import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

if n < 2:
    sys.stdout.write(str(-1))
    sys.exit()

max_prod = max(arr) * max(arr)
targets = set()
for start in range(1, 10):
    val = 0
    for d in range(start, 10):
        val = val * 10 + d
        if val > max_prod:
            break
        targets.add(val)

result = -1
for i in range(n):
    ai = arr[i]
    for j in range(i + 1, n):
        p = ai * arr[j]
        if p in targets and p > result:
            result = p

sys.stdout.write(str(result))