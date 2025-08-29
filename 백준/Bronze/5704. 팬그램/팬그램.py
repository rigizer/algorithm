import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
while True:
    words = input()
    if words == '*':
        break
    alphabet = [False] * 26

    for i in words:
        if i == ' ':
            continue
        alphabet[ord(i) - 97] = True

    result.append('N' if False in alphabet else 'Y')

print('\n'.join(result))