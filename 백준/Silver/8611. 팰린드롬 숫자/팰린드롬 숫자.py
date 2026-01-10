import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
results = []

for base in range(2, 11):
    temp = n
    digits = []
    while temp > 0:
        temp, r = divmod(temp, base)
        digits.append(str(r))
    digits = ''.join(reversed(digits))
    if digits == digits[::-1]:
        results.append(f'{base} {digits}')

if results:
    print('\n'.join(results))
else:
    print('NIE')