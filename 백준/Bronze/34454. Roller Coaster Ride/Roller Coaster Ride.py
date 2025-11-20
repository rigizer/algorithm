import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
c = int(input())
p = int(input())

capacity = c * p

if n <= capacity:
    result = 'yes'
else:
    result = 'no'

print(result)