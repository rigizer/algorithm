import itertools

words = [input() for _ in range(6)]
perms = list(itertools.permutations(words))

for p in perms:
    puzzle = [[None] * 3 for _ in range(3)]
    find = True
    for i, v in enumerate(p):
        if i // 3 == 0:
            for j in range(3):
                puzzle[i % 3][j] = v[j]
        else:
            for j in range(3):
                if puzzle[j][i % 3] != v[j]:
                    find = False
                    break
                puzzle[j][i % 3] = v[j]

    if find == True:
        print('\n'.join([str(''.join(t)) for t in puzzle]))
        exit(0)

print(0)