tc = int(input())
for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    s = len(data)
    avg = sum(data) / s
    avg = int(avg) + 1 if avg - int(avg) >= 0.5 else int(avg)
    print(f'#{t} {avg}')