n = int(input())
m = int(input())

s = [0 for i in range(n + 1)]
for i in range(2, n + 1):
    if s[i] == 0:
        for t in range(i, n + 1, i):
            if t % i == 0:
                s[t] = max(s[t], i)
result = 0
for i in s:
    if i <= m:
        result += 1
print(result - 1)