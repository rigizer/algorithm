from collections import Counter

n = int(input())
for _ in range(n):
    s = input()
    cnt = 0
    for i in Counter(s):
        if i.lower() == 'g':
            cnt += Counter(s)[i]
        elif i.lower() == 'b':
            cnt -= Counter(s)[i]
    if cnt > 0:
        print(s + ' is GOOD')
    elif cnt == 0:
        print(s + ' is NEUTRAL')
    elif cnt < 0:
        print(s + ' is A BADDY')