import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
names = [input() for _ in range(k)]

l = len(names[0])
values = [int(x) for x in names]

min_n = max(max(values), 10 ** (l - 1))
max_n = 10 ** l - 1

print(min_n)
print(max_n)