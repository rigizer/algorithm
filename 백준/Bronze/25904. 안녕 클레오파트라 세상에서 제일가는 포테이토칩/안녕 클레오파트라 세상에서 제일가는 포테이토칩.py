n, x = map(int, input().split())
t = list(map(int, input().split()))
check = True
while check:
    for i in range(n):
        if x <= t[i]:
            x += 1
        else:
            result = i
            check = False
            break
print(result + 1)