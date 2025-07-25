n = int(input())
mine = [0] + [int(input()) for _ in range(n)] + [0]

result = []
for i in range(1, n + 1):
    if mine[i - 1] <= mine[i] >= mine[i + 1]:
        result.append(i)

print('\n'.join(map(str, result)))