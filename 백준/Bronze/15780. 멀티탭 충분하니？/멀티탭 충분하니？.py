n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
for i in a:
    if i % 2 == 0:
        sum += i / 2
    else:
        sum += int(i / 2) + 1

print('YES' if n <= sum else 'NO')