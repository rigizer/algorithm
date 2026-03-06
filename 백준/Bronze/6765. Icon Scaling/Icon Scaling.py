import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())

icon = [
    '*x*',
    ' xx',
    '* *'
]

for row in icon:
    line = ''
    for ch in row:
        line += ch * k
    for _ in range(k):
        print(line)