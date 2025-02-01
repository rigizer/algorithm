score = 0
mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))

for i in range(10):
    ex_score = score
    score += mushrooms[i]
    if score >= 100:
        under = 100 - ex_score
        over = score - 100
        if over <= under:
            print(score)
            break
        else:
            print(ex_score)
            break
else:
    print(score)