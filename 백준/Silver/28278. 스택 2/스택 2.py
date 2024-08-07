import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    op = list(map(int, input().split()))
    
    if (op[0] == 1):
        stack.append(op[1])
    elif (op[0] == 2):
        if (len(stack) > 0):
            print(stack.pop())
        else:
            print(-1)
    elif (op[0] == 3):
        print(len(stack))
    elif (op[0] == 4):
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    else:
        if (len(stack) > 0):
            print(stack[-1])
        else:
            print(-1)