n, l = map(int, input().split())
counts = []

for _ in range(n):
    s = input()
    count = 0
    i = 0
    while i < l:
        if s[i] == '1':
            count += 1
            while i < l and s[i] == '1':
                i += 1
        else:
            i += 1
    counts.append(count)

max_count = max(counts)
zebra_count = counts.count(max_count)
print(max_count, zebra_count)