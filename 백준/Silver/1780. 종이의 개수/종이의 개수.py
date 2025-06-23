n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

count = {-1: 0, 0: 0, 1: 0}

def divide(x, y, size):
    num = paper[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != num:
                same = False
                break
        if not same:
            break

    if same:
        count[num] += 1
    else:
        new_size = size // 3
        for dx in range(3):
            for dy in range(3):
                divide(x + dx * new_size, y + dy * new_size, new_size)

divide(0, 0, n)

print(count[-1])
print(count[0])
print(count[1])