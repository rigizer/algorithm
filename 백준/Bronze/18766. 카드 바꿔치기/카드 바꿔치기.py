import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    before = input().split()
    after = input().split()
    
    count = {}
    
    for card in before:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    
    for card in after:
        if card in count:
            count[card] -= 1
        else:
            count[card] = -1
    
    result = 'NOT CHEATER'
    for v in count.values():
        if v != 0:
            result = 'CHEATER'
            break
    
    print(result)