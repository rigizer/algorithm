import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
levels = list(map(int, input().split()))

result = []
for m in levels:
    if m == 300:
        result.append('1')
    elif m >= 275:
        result.append('2')
    elif m >= 250:
        result.append('3')
    else:
        result.append('4')

print(*result)