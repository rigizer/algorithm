from itertools import permutations

n = int(input())
men = [input().strip() for _ in range(n)]
women = [input().strip() for _ in range(n)]

def score(a, b):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
    return cnt

result = 0
for perm in permutations(women):
    total = 0
    for i in range(n):
        total += score(men[i], perm[i])
    if total > result:
        result = total

print(result)