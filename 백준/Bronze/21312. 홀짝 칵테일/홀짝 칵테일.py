cocktail = list(map(int, input().split()))
check = False
result = 1

for i in range(3):
    if cocktail[i] % 2 != 0:
        result *= cocktail[i]
        check = True

if check:
    print(result)
else:
    print(cocktail[0] * cocktail[1] * cocktail[2])