question = input()
stack = []
answer = 0

for idx in range(len(question)):
    if question[idx] == '(':
        stack.append('(')
    else:
        stack.pop()
        if question[idx-1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)