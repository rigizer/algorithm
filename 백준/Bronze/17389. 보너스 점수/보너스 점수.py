n, s = input(), input()
score, bonus = 0, 0

for idx, ox in enumerate(s):
    if ox == 'O':
        score, bonus = score + idx + 1 + bonus, bonus + 1
    else:
        bonus = 0

print(score)