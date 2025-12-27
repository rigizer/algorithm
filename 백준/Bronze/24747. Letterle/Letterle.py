import sys
input = lambda: sys.stdin.readline().rstrip()

answer = input()
guesses = [input() for _ in range(7)]

for i in range(7):
    guess = guesses[i]
    if guess == answer:
        print('WINNER')
        break

    result = [''] * 5
    for j in range(5):
        if guess[j] == answer[j]:
            result[j] = 'G'
    for j in range(5):
        if result[j] == '' and guess[j] not in answer:
            result[j] = 'X'
    for j in range(5):
        if result[j] == '':
            result[j] = 'Y'

    if i == 6:
        print('LOSER')
    else:
        print(''.join(result))