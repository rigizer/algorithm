import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
result = []

for ds in range(1, K + 1):
    n, m, T = map(int, input().split())
    donations = [0.0] * (n + 1)

    for _ in range(m):
        parts = input().split()
        i = int(parts[0])
        t = int(parts[1])
        d = float(parts[2])

        diff = T - t
        if 0 <= diff < 1000:
            donations[i] += d

    total_for = 0.0
    total_against = 0.0

    for i in range(1, n + 1):
        vote = input().strip()
        if vote == 'Y':
            total_for += 1.0
        else:
            D = donations[i]
            total_against += 1.0 / (1.0 + (D / 10000.0))

    result.append(f'Data Set {ds}:\n')
    result.append(f'{total_for:.2f} {total_against:.2f}\n\n')

print(''.join(result))