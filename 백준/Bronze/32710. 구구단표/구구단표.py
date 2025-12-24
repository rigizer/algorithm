import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
found = False

for a in range(2, 10):
    for b in range(1, 10):
        found = True if a * b == n else found

found = True if 1 <= n <= 9 else found
print(1 if found else 0)