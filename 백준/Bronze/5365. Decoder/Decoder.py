n = int(input())
words = list(map(str, input().split()))

result = ''
index = 0

for i in range(n):
    if i == 0:
        result += words[i][0]
        index = len(words[i])
    else:
        if len(words[i]) >= index:
            result += words[i][index - 1]
            index = len(words[i])
        else:
            result += ' '
            index = len(words[i])

print(result)