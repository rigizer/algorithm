import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

counter = Counter(a)
max_count = max(counter.values())

if max_count <= (n + 1) // 2:
    print('YES')
else:
    print('NO')