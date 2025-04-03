import math
from collections import deque

def bfs(n, a, b, is_prime):
    max_limit = max(n, b)
    queue = deque()
    visited = [False] * (max_limit + 1)

    queue.append((n, 0))
    visited[n] = True

    while queue:
        x, t = queue.popleft()

        if a <= x <= b and is_prime[x]:
            return t
    
        for d in (x // 2, x // 3, x + 1, x - 1):
            if 0 <= d <= max_limit and not visited[d]:
                queue.append((d, t + 1))
                visited[d] = True

    return -1

num = 1_000_000
is_prime = [True] * (num + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(num)) + 1):
    if is_prime[i]:
        for j in range(i * i, num + 1, i):
            is_prime[j] = False

result = []
for tc in range(int(input())):
    n, a, b = map(int, input().split())
    result.append(bfs(n, a, b, is_prime))

print('\n'.join(map(str, result)))