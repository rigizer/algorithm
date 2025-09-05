import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    cnt = 0
    s = input()
    if s == '#':
        break
    for c in s:
        if c == 'e':
            print(s[:-1], end='')
            print(1 if cnt % 2 != 0 else 0)
        elif c == 'o':
            print(s[:-1], end='')
            print(1 if cnt % 2 == 0 else 0)
        else:
            cnt += 1 if c == '1' else 0