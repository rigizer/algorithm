import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for tc in range(1, t + 1):
    g = [[0] * 3 for _ in range(3)]
    
    g[0] = list(map(int, input().split()))
    a, b = map(int, input().split())
    g[1][0] = a
    g[1][2] = b
    g[2] = list(map(int, input().split()))
    
    result = 0
    if g[0][1] - g[0][0] == g[0][2] - g[0][1]:
        result += 1
    if g[2][1] - g[2][0] == g[2][2] - g[2][1]:
        result += 1
    if g[1][0] - g[0][0] == g[2][0] - g[1][0]:
        result += 1
    if g[1][2] - g[0][2] == g[2][2] - g[1][2]:
        result += 1
    
    from collections import defaultdict
    cnt = defaultdict(int)
    
    s = g[0][1] + g[2][1]
    if s % 2 == 0:
        cnt[s // 2] += 1
    s = g[1][0] + g[1][2]
    if s % 2 == 0:
        cnt[s // 2] += 1
    s = g[0][0] + g[2][2]
    if s % 2 == 0:
        cnt[s // 2] += 1
    s = g[0][2] + g[2][0]
    if s % 2 == 0:
        cnt[s // 2] += 1
    
    max_center = 0
    for v in cnt.values():
        if v > max_center:
            max_center = v
    result += max_center
    
    print(f'Case #{tc}: {result}')