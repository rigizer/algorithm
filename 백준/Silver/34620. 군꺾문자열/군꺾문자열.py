import sys
input = lambda: sys.stdin.readline().rstrip()

x = 0
a, b = map(int, input().split())
result = []

while True:
    if a - b > 0:
        a -= b
        result += 'G'
    elif b % 2 == 0:
        b //= 2
        result += 'K'
    else:
        print(-1)
        exit(0)
    
    if a == 1 and b == 1:
        result += 'G'
        break

print(''.join(reversed(result)))