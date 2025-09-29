from itertools import permutations

n = int(input())
games = [tuple(map(int, input().split())) for _ in range(n)]

win = {(0, 2), (1, 0), (2, 1)}

max_win = 0

for perm in permutations([0, 1, 2]):
    count = 0
    for a, b in games:
        a_gesture = perm[a - 1]
        b_gesture = perm[b - 1]
        if (a_gesture, b_gesture) in win:
            count += 1
    if count > max_win:
        max_win = count

print(max_win)