import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
heights = [int(input()) for _ in range(n)]

avg = sum(heights) // n
result = 0
for h in heights:
    if h < avg:
        result += avg - h

print(result)