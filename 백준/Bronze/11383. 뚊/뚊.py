import sys
input = lambda: sys.stdin.readline().rstrip()

def check(a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j * 2]:
                return False
            if a[i][j] != b[i][j * 2 + 1]:
                return False
    return True

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]
result = check(a, b)
print('Eyfa' if result else 'Not Eyfa')