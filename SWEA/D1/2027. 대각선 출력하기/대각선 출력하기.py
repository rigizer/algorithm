arr = [['+'] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i == j:
            arr[i][j] = '#'
    print(''.join(arr[i]))