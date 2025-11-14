import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = str(n)
m = len(s)

if n == 0:
    print(1)
    exit()

def max_repeat(d):
    for k in range(m, 0, -1):
        if int(str(d) * k) <= n:
            return k
    return 0

max_counts = []
max_zero = max(1, m - 1)
max_counts.append(max_zero)

max6 = max_repeat(6)
max9 = max_repeat(9)
combined_69_packs = (max6 + max9 + 1) // 2

for d in range(1, 10):
    if d == 6 or d == 9:
        continue
    max_counts.append(max_repeat(d))

result = max(max(max_counts), combined_69_packs)
print(result)