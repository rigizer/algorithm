n, m = map(int, input().split())
ball = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    ball[i], ball[j] = ball[j], ball[i]

print(' '.join(str(ball[i]) for i in range(1, n + 1)))