tc = int(input())
for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    s = [i if i % 2 == 1 else 0 for i in data]
    print(f'#{t} {sum(s)}')