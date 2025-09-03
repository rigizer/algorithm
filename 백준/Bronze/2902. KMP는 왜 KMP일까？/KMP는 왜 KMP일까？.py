import sys
input = lambda: sys.stdin.readline().rstrip()

s = input().split('-')
print(''.join([i[0] for i in s]))