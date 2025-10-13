import sys
input = lambda: sys.stdin.readline().rstrip()

n, a, b = map(int,input().split())
h = [list(map(int,input().split())) for _ in range(10)]

if b >= 130 and a >= 66:
    print('Nice')
else:
    for i in range(8-n):
        a += h[i][0] * 3
        b += h[i][0] * 3
        score = 6 - h[i][0]
        if score < h[i][1]:
            b += score * 3
        else:
            b += h[i][1] * 3
        score = 6

    if b >= 130 and a >= 66:
        print('Nice')
    else:
        print('Nae ga wae')