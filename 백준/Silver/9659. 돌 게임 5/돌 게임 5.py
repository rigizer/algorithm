import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
print('SK' if n % 2 == 1 else 'CY')