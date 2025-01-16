lst = [0] * 10001
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        lst[i] = 1
print(sum(lst))