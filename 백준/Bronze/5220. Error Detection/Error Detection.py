import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for i in range(t):
    value, check = map(int, input().split())
    cnt = bin(value).count('1')
    
    if cnt % 2 == check:
        result = 'Valid'
    else:
        result = 'Corrupt'
    
    if i == t - 1:
        print(result)
    else:
        print(result)