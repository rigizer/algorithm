import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    b, x, y = map(int, input().split())
    
    result = 0
    mul = 1
    
    while x > 0 or y > 0:
        dx = x % b
        dy = y % b
        
        digit = (dx + dy) % b
        
        result += digit * mul
        
        x //= b
        y //= b
        mul *= b
    
    print(result)