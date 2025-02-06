from itertools import combinations

n, m, k = map(int,input().split())
answer = 0
all = [*combinations([i for i in range(n)], m)]

for i in all:
    count = 0
    for j in range(m):
        if i[j] < m:
            count += 1
    if count >= k:
        answer += 1

print(answer / len(all))