import sys
input = lambda: sys.stdin.readline().rstrip()

start, days = map(int, input().split())
week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
print(' '.join(week))

result = []
line = []
for _ in range(start - 1):
    line.append('   ')
for d in range(1, days + 1):
    line.append(f'{d:>3}')
    if len(line) == 7:
        result.append(' '.join(line).rstrip())
        line = []
if line:
    result.append(' '.join(line).rstrip())

print('\n'.join(result))