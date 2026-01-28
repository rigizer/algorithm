import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
events = input()

rooms = [0] * 10

for e in events:
    if e == 'L':
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break
    elif e == 'R':
        for i in range(9, -1, -1):
            if rooms[i] == 0:
                rooms[i] = 1
                break
    else:
        rooms[int(e)] = 0

print(''.join(map(str, rooms)))