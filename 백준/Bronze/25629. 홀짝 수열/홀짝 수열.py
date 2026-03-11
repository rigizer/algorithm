import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

odd_cnt = 0
even_cnt = 0

for x in a:
    if x % 2 == 1:
        odd_cnt += 1
    else:
        even_cnt += 1

odd_pos = (n + 1) // 2
even_pos = n // 2

if odd_cnt == odd_pos and even_cnt == even_pos:
    print(1)
else:
    print(0)