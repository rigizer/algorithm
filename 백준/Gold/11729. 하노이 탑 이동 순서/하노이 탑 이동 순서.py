result = 0
move = []
def hanoi(n, from_pos, to_pos, aux_pos):
    global result
    result += 1
    if n == 1:
        move.append((from_pos, to_pos))
        return
    
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    move.append((from_pos, to_pos))
    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(int(input()), 1, 3, 2)
print(result)
print('\n'.join(' '.join([str(i), str(j)]) for i, j in move))