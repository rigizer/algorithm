import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
result = []

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    prices.sort(reverse=True)
    
    discount = 0
    
    for i in range(2, n, 3):
        discount += prices[i]
    
    result.append(str(discount))

print('\n'.join(result))