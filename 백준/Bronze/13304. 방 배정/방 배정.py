import math

n, k = map(int, input().split())
student = [0, 0, 0, 0, 0]

for _ in range(n):
    s, y = map(int, input().split())
    if y == 1 or y == 2:
        student[0] += 1
    elif s == 0 and (y == 3 or y == 4):
        student[1] += 1
    elif s == 1 and (y == 3 or y == 4):
        student[2] += 1
    elif s == 0 and (y == 5 or y == 6):
        student[3] += 1
    else:
        student[4] += 1
        
room = 0
for i in student:
    room += math.ceil(i / k)
print(room)