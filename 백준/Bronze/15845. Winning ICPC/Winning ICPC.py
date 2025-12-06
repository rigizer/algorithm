import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
t = list(map(int, input().split()))

best_team = 1
best_count = -1

for i in range(1, n + 1):
    scores = list(map(int, input().split()))
    count = 0

    for j in range(m):
        if scores[j] == t[j]:
            count += 1

    if count > best_count:
        best_count = count
        best_team = i

print(best_team)