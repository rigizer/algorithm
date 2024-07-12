n = int(input())
lst = list(map(int, input().split()))

res = 0
first = lst[0]
pre = lst[0]

for i in lst[1:]:
    if i != pre + 1:
        res += first
        first = i
    pre = i

res += first
print(res)