import sys
input = lambda: sys.stdin.readline().rstrip()

lines = sys.stdin.readlines()
result = []

for line in lines:
    s = line.rstrip('\n')
    while 'BUG' in s:
        s = s.replace('BUG', '')
    result.append(s)

print('\n'.join(result))