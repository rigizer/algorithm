answer = 0
n = int(input())
for number in range(1, n + 1):
    if number ** 2 <= n:
        answer += 1
print(answer)