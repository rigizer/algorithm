import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
expression = input()
v = [int(input()) for _ in range(n)]
stack = []

for ch in expression:
    if 'A' <= ch <= 'Z':
        stack.append(v[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)

result = stack[0]
print(f'{result:.2f}')