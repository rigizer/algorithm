import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = []

for _ in range(n):
    x = int(input())
    base = 10
    
    while base <= x:
        x = (x + base // 2) // base * base
        base *= 10
    result.append(str(x))

print('\n'.join(result))