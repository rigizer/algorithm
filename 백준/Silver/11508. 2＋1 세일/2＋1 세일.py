n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))
c.sort(reverse=True)

result = 0
for i in range(2, len(c), 3):
    result += c[i]

print(sum(c) - result)