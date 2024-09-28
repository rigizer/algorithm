n = int(input())
m = int(input())

positions = list(map(int, input().split()))
len_positions = len(positions)

min_height = 0

if len_positions == 1:
    min_height = max(positions[0] - 0, n - positions[0])
else:
    for i in range(len_positions):
        if i == 0:
            height = positions[i] - 0
        elif i == len_positions - 1:
            height = n - positions[i]
        else:
            tmp = positions[i] - positions[i - 1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        min_height = max(height, min_height)

print(min_height)