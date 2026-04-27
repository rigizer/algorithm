import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def sieve():
    prime = [True] * 10000
    prime[0] = prime[1] = False
    for i in range(2, 100):
        if prime[i]:
            for j in range(i * i, 10000, i):
                prime[j] = False
    return prime

prime = sieve()

t = int(input())
result = []

for _ in range(t):
    a, b = input().split()
    if a == b:
        result.append('0')
        continue

    visited = [False] * 10000
    q = deque()
    q.append((a, 0))
    visited[int(a)] = True

    found = False

    while q:
        cur, cnt = q.popleft()

        for i in range(4):
            for d in '0123456789':
                if i == 0 and d == '0':
                    continue
                if cur[i] == d:
                    continue

                nxt = cur[:i] + d + cur[i + 1:]
                num = int(nxt)

                if not visited[num] and prime[num]:
                    if nxt == b:
                        result.append(str(cnt + 1))
                        found = True
                        break
                    visited[num] = True
                    q.append((nxt, cnt + 1))
            if found:
                break
        if found:
            break

    if not found:
        result.append('Impossible')

for x in result:
    print(x)