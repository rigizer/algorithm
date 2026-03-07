import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dna = [input() for _ in range(n)]

result = []
distance = 0
order = ['A', 'C', 'G', 'T']

for j in range(m):
    count = {c: 0 for c in order}

    for i in range(n):
        count[dna[i][j]] += 1

    best_char = 'A'
    best_count = -1

    for c in order:
        if count[c] > best_count:
            best_count = count[c]
            best_char = c

    result.append(best_char)
    distance += n - best_count

print(''.join(result))
print(distance)