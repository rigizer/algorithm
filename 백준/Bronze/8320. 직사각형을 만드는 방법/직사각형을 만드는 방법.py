square = 0
for i in range(1, int(input()) + 1):
    check = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            if j in check:
                break
            else:
                square += 1
                check.append(i // j)
    square += 1
print(square)