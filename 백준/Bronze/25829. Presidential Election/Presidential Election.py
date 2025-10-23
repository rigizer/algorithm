import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
vote1 = vote2 = 0
electoral1 = electoral2 = 0

for _ in range(n):
    e, v1, v2 = map(int, input().split())
    vote1 += v1
    vote2 += v2
    if v1 > v2:
        electoral1 += e
    else:
        electoral2 += e

majority = 1 if vote1 > vote2 else 2 if vote2 > vote1 else 0
electoral = 1 if electoral1 > electoral2 else 2 if electoral2 > electoral1 else 0

if majority == electoral == 1:
    print(1, end='')
elif majority == electoral == 2:
    print(2, end='')
else:
    print(0, end='')