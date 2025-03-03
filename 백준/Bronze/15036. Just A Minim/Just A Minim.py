n = int(input())
s = list(map(int, input().split()))

sheet = {
    0: 32, 1: 16, 2: 8, 4: 4, 8: 2, 16: 1
}

result = sum([sheet[i] for i in s])
print(result // 16 if result % 16 == 0 else result / 16)