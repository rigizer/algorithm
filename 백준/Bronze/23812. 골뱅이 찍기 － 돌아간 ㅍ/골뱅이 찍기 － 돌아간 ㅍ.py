import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
snail = [['@', ' ', ' ', ' ', '@'], ['@', '@', '@', '@', '@'], ['@', ' ', ' ', ' ', '@'], ['@', '@', '@', '@', '@'], ['@', ' ', ' ', ' ', '@']]

for i in range(5):
    for j in range(n):
        for x in range(5):
            for y in range(n):
                print(snail[i][x], end='')
        print()