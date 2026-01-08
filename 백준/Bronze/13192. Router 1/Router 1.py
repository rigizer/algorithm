import sys
input = lambda: sys.stdin.readline().rstrip()

n, m_lim, p_lim = map(int, input().split())

hub = 2 * n + 1
n_tot = 2 * n + 1
m = 2 * n

result = []
result.append(f'{n_tot} {m}')

for i in range(1, n + 1):
    result.append(f'{i} {hub}')

for j in range(n + 1, 2 * n + 1):
    result.append(f'{hub} {j}')

print('\n'.join(result))