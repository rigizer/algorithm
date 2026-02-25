import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
prev_a, prev_b = None, None
ok = True

for _ in range(n):
    a, b = map(int, input().split())
    if prev_a is not None:
        if a < prev_a or b < prev_b:
            ok = False
            break
    prev_a, prev_b = a, b

print('yes' if ok else 'no')