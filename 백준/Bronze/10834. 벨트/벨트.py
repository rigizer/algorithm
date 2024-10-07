m = int(input())
answer = 0
rotate = 0

for i in range(m):
    a, b, r = map(int, input().split())
    
    if i == 0:
        answer = a * b
    else:
        answer = int(answer / a * b)
    if r == 1:
        rotate = 1 - rotate
    
print(rotate, answer)