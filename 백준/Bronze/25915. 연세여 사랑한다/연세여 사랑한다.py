c = input()
pwd = 'ILOVEYONSEI'

answer = 0
for i in pwd:
    answer += abs(ord(c) - ord(i))
    c = i
print(answer)