import sys
input = lambda: sys.stdin.readline().rstrip()

result = 0
n = int(input())

is_gold = True

for _ in range(n):
    a = int(input())
    b = int(input())
    r = (a * 5) - (b * 3)
    
    if r > 40:
        result += 1
    
    if is_gold and r <= 40:
        is_gold = False

print(''.join([str(result), '+' if is_gold else '']))