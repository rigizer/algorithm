x, y = 0, 0
for _ in range(int(input())):
    w = input()
    if w == 'D':
        x += 1
    elif w == 'P':
        y += 1

    if abs(x - y) >= 2:
        break

print(f'{x}:{y}')