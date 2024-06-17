import sys
sys.setrecursionlimit(100_000)

n, m, k = map(int, input().split())
student = [0] + list(map(int, input().split()))
friend = [[] for _ in range(n + 1)]

for _ in range(m):
    v, w = map(int, input().split())
    friend[v].append(w)
    friend[w].append(v)

visited = [False] * (n + 1)
friends = []

def dfs(v, arr):
    for i in friend[v]:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(i, arr)

for i in range(1, n + 1):
    if not visited[i]:
        arr = [i]
        visited[i] = True
        dfs(i, arr)
        friends.append(arr)

result = 0

for f in friends:
    cost = 1 << 60
    for j in f:
        if cost > student[j]:
            cost = student[j]
    
    result += cost

if result <= k:
    print(result)
else:
    print('Oh no')