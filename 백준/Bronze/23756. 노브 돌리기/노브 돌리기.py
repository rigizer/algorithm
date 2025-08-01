n = int(input())
start = int(input())
result = 0
for i in range(n):
    go = int(input())
    result += min(abs(start - go), 360 - start + go, start + 360 - go)
    start = go
print(result)