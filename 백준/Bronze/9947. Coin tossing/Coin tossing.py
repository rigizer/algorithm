import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    a, b = input().split()
    if a == '#' and b == '#':
        break
    
    n = int(input())
    score_a = 0
    score_b = 0
    
    for _ in range(n):
        call, result = input().split()
        if call == result:
            score_a += 1
        else:
            score_b += 1
    
    print(a, score_a, b, score_b)