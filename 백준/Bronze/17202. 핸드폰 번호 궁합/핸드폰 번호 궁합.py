a = list(input())
b = list(input())
temp = []
answer = ''
 
for i in range(8):
    answer += a[i] + b[i]
 
while len(answer) != 2:
    for i in range(len(answer) - 1):
        temp.append(str((int(answer[i]) + int(answer[i + 1])) % 10))
    answer = ''.join(temp)
    temp = []

print(answer)