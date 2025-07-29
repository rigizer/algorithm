n = int(input())
sa = [input() for _ in range(n)]
an = [input() for _ in range(n)]

result = 0
for i in range(n):
    if sa[i] == an[i]:
        result += 1
print(result)