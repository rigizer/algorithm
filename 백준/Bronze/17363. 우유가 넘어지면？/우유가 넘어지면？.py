import sys
input = lambda: sys.stdin.readline().rstrip()

d = {'.': 46, 'O': 79, '-': 124, '|': 45, '/': 92, '\\': 47, '^': 60, '<': 118, 'v': 62, '>': 94}

n, m = map(int, input().split())
box = []
for _ in range(n):
    box.append(input())

rotate = []
for i in range(m - 1, -1, -1):
    row = []
    for j in range(n):
        row.append('%c' % d[box[j][i]])
    rotate.append(row)

for r in rotate:
    print(''.join(r))