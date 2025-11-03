import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    num = int(input())

    if num == 0:
        break
    
    roll = 0
    for i in range(num):
        line = input()
        line += ' '
        
        idx = []
        for j in range(len(line)):
            if line[j] == ' ':
                idx.append(j)
            
        if i == 0:
            roll = idx[0]
            
        for k in range(len(idx)):
            if idx[k] >= roll:
                roll = idx[k]
                break
    print(roll + 1)