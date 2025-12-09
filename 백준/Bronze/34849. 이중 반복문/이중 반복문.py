import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
limit = 10**8

if n ** 2 <= limit:
    print('Accepted')
else:
    print('Time limit exceeded')