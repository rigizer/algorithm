import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = True

for _ in range(n):
    height = int(input())
    if height < 48:
        result = False
        break

print(result)