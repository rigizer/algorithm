import sys
input = lambda: sys.stdin.readline().rstrip()

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

position = k

for _ in range(m):
    x = int(input())

    if x > 0:
        left = 1
        right = x
        if left <= position <= right:
            position = left + right - position

    else:
        length = -x
        left = n - length + 1
        right = n
        if left <= position <= right:
            position = left + right - position

print(position)