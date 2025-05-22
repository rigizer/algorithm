n = int(input())

dice = [[0, 1, 3, 6, 10, 15], [0, 6, 11, 15, 18, 20]]
result = 0

for i in range(2):
    result += (
    dice[i][5]
    + dice[i][4] * (2 * (n - 1))
    + dice[i][2] * (n - 1)
    + (dice[i][1] * 2 + dice[i][3]) * ((n - 2) * (n - 1) // 2)
    )

print(result)