tc = int(input())
for t in range(1, tc + 1):
    p, q, r, s, w = map(int, input().split())
    print(f'#{t} {min(p * w, q + max(0, w - r) * s)}')