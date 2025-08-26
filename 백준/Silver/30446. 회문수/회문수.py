n = int(input())

result = []
odd = [str(i) for i in range(10)]
even = [i+i for i in odd]

result = odd + even
temp1 = result[:]

for _ in range(4):
    temp2 = []
    temp3 = []
    for i in temp1:
        for j in range(10):
            x = str(j) + i + str(j)
            temp2.append(x)
            if j != 0:
                temp3.append(x)
    result.extend(temp3)
    temp1 = temp2[:]

result.remove('0')
result.remove('00')

answer = []
for i in result:
    x = int(i)
    if x <= n:
        answer.append(x)

print(len(answer))