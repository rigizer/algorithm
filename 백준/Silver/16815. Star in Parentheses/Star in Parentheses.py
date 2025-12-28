import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
n = len(s)
star = s.index('*')

def is_balanced(sub):
    cnt = 0
    for c in sub:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

result = 0

for l in range(star):
    if s[l] != '(':
        continue
    for r in range(star + 1, n):
        if s[r] != ')':
            continue
        middle = s[l + 1:r].replace('*', '')
        if is_balanced(middle):
            result += 1

print(result)