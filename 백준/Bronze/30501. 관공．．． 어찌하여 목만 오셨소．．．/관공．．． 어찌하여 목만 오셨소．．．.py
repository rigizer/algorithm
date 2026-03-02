import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

result = ''
for _ in range(n):
    name = input()
    if 'S' in name:
        result = name

print(result)