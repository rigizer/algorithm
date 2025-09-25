import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
levels = [int(input()) for _ in range(n)]

levels.sort(reverse=True)

if n > 42:
    levels = levels[:42]

level_sum = sum(levels)
stat_sum = 0

for level in levels:
    if level >= 60:
        stat_sum += 1
    if level >= 100:
        stat_sum += 1
    if level >= 140:
        stat_sum += 1
    if level >= 200:
        stat_sum += 1
    if level >= 250:
        stat_sum += 1

print(level_sum, stat_sum)