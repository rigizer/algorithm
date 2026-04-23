import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
s = s.replace('-', '+-')
terms = s.split('+')
result = 0
for term in terms:
    if not term:
        continue
    if 'x' in term:
        coef = term.replace('x', '')
        if coef == '' or coef == '+':
            coef = 1
        elif coef == '-':
            coef = -1
        else:
            coef = int(coef)
        result += coef
print(result)