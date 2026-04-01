import sys
input = lambda: sys.stdin.readline().rstrip()

case = 1

while True:
    line = input()
    if not line:
        continue
    
    n = int(line)
    if n < 0:
        break
    
    total_mass = 0
    sum_x = 0
    sum_y = 0
    
    for _ in range(n):
        x, y, m = map(int, input().split())
        
        total_mass += m
        sum_x += x * m
        sum_y += y * m
    
    a = sum_x / total_mass
    b = sum_y / total_mass
    
    print(f'Case {case}: {a:.2f} {b:.2f}')
    
    case += 1