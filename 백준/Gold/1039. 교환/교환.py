import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n, k = input().split()
k = int(k)

if len(n) == 1:
    print(-1)
    exit()

queue = deque()
queue.append(n)

visited = [set() for _ in range(k + 1)]
visited[0].add(n)

for depth in range(k):
    for _ in range(len(queue)):
        cur = queue.popleft()
        cur_list = list(cur)

        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]

                if cur_list[0] != '0':
                    nxt = ''.join(cur_list)
                    if nxt not in visited[depth + 1]:
                        visited[depth + 1].add(nxt)
                        queue.append(nxt)

                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]

if not visited[k]:
    print(-1)
else:
    print(max(visited[k]))