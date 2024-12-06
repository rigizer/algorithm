n = int(input())
s = input()
result = ''

for i in s:
    if i == 'I':
        result += 'i'
    elif i == 'l':
        result += 'L'

print(result)