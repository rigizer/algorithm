result = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+': result += n;
    elif op == '-': result -= n;
    elif op == '*': result *= n;
    elif op == '/': result //= n;
print(result)