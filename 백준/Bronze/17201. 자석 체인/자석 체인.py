import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()

is_connected = True

for i in range(n - 1):
    right_pole = s[2 * i + 1]
    next_left_pole = s[2 * i + 2]
    
    if right_pole == next_left_pole:
        is_connected = False
        break

if is_connected:
    print('Yes')
else:
    print('No')