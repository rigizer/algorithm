cnt = 1
while True:
    num1, cmd, num2 = input().split()
    if cmd == 'E':
        break
    if cmd == '!=':
        print('Case {}: '.format(cnt) + str(int(num1) != int(num2)).lower())
    elif cmd == '<':
        print('Case {}: '.format(cnt) + str(int(num1) < int(num2)).lower())
    elif cmd == '<=':
        print('Case {}: '.format(cnt) + str(int(num1) <= int(num2)).lower())
    elif cmd == '>':
        print('Case {}: '.format(cnt) + str(int(num1) > int(num2)).lower())
    elif cmd == '>=':
        print('Case {}: '.format(cnt) + str(int(num1) >= int(num2)).lower())
    elif cmd == '==':
        print('Case {}: '.format(cnt) + str(int(num1) == int(num2)).lower())
    cnt += 1