import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

result = max(size[1:])
print(result)