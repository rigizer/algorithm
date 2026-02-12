import sys
input = lambda: sys.stdin.readline().rstrip()

w = input()

cnt = 0
target = ord('i') - ord('a')

for shift in range(26):
    ok = True
    for ch in w:
        x = ord(ch) - ord('a')
        y = (x + shift) % 26
        if y == target:
            ok = False
            break
    if ok:
        cnt += 1

if cnt == 0:
    print('impossible')
else:
    print(str(cnt))