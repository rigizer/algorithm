t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    if m < 4 or n < 12:
        print(-1)
    else:
        print(11 * m + 4)