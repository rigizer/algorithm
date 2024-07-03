subcode = input()
n = int(input())
result = 0

for _ in range(n):
    avaliable = input()
    if subcode[:5] == avaliable[:5]:
        result += 1

print(result)