import sys
input = lambda: sys.stdin.readline().rstrip()

t_line = input()
if t_line == '':
    sys.exit(0)

t = int(t_line)
result = []

for i in range(1, t + 1):
    n = int(input())
    a, b = map(int, input().split())
    for _ in range(n):
        input()
    result.append(f'Material Management {i}')
    result.append('Classification ---- End!')

print('\n'.join(result))