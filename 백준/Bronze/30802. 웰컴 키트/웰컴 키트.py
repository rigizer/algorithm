n = int(input())
ex = list(map(int,input().split()))
t, p = map(int,input().split())

ans = 0
for e in ex:
    if e % t == 0:
        ans += int(e / t)
    else:
        ans += (int(e / t) + 1)

print(ans)

ans2 = [int(sum(ex) / p), sum(ex) % p]
print(*ans2)