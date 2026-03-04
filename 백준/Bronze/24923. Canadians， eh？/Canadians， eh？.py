import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()

if s.endswith('eh?'):
    print('Canadian!')
else:
    print('Imposter!')