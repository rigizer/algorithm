n, s = input().split()
n = int(n)

chat_log = []
for _ in range(n):
    nickname, message = input().split()
    chat_log.append((nickname, message))

answer_message = ''
for nickname, message in chat_log:
    if nickname == s:
        answer_message = message
        break

count = 0
for nickname, message in chat_log:
    if nickname == s:
        break
    if message == answer_message:
        count += 1

print(count)