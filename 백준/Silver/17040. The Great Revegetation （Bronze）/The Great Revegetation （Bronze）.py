import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

color = [0] * n

for i in range(n):
    used = set()
    for v in adj[i]:
        if color[v] != 0:
            used.add(color[v])
    for c in range(1, 5):
        if c not in used:
            color[i] = c
            break

print(''.join(map(str, color)))