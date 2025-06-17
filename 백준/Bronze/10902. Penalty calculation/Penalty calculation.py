n = int(input())
submissions = []

for _ in range(n):
    t, s = map(int, input().split())
    submissions.append((t, s))

max_score = max(s for t, s in submissions)

for idx, (t, s) in enumerate(submissions):
    if s == max_score:
        f = idx + 1
        tf = t
        sf = s
        break

if sf == 0:
    print(0)
elif sf == 1 or sf == 4:
    penalty = tf + (f - 1) * 20
    print(penalty)
else:
    print(0)