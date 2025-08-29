while True:
    words = input()
    if words == '*':
        break
    alphabet = [False] * 26

    for i in words:
        if i == ' ':
            continue
        alphabet[ord(i) - 97] = True

    print('N' if False in alphabet else 'Y')