import sys
input = lambda: sys.stdin.readline().rstrip()

case = 1
result = []
while True:
    a, b  = input(), input()
    if a == 'END':
        break
    
    result.append(f'Case {case}: {'same' if sorted(a) == sorted(b) else 'different'}')
    case += 1

print('\n'.join(result))