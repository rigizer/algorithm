white = {'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}
black = {'k': 0, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}
chess = [input() for _ in range(8)]

w = 0
b = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] in white.keys():
            w += white.get(chess[i][j])
        elif chess[i][j] in black.keys():
            b += black.get(chess[i][j])

print(w - b)