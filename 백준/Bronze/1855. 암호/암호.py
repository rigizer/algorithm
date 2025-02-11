k = int(input())
temp = input()
num = len(temp) // k
array = [[] for _ in range(k)]

for i in range(1, num + 1):
    if i % 2 == 1:
        for j in range(k):
            array[j].append(temp[j])
        temp = temp[k:]
    else:
        for j in range(k):
            array[j].append(temp[k - j - 1])
        temp = temp[k:]

answer = ''
for arr in array:
    for i in arr:
        answer += i
print(answer)