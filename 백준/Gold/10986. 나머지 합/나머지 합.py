n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]

count = [0] * m
answer = 0

for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        answer += 1
    count[remainder] += 1

for c in count:
    if c > 1:
        answer += c * (c - 1) // 2

print(answer)