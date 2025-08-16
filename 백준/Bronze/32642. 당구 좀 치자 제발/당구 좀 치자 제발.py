n = int(input())
weather = list(map(int, input().split()))

val = -1 if weather[0] == 0 else 1
result = val
for i in range(1, n):
    val += -1 if weather[i] == 0 else 1
    result += val

print(result)