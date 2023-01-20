score = []
for _ in range(5):
    s = int(input())
    if s < 40:
        score.append(40)
    else:
        score.append(s)

print(sum(score) // 5)