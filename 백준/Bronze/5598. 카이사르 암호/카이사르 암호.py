word = [chr(((ord(i) - 65 - 3) + 26) % 26 + 65) for i in input()]
print(''.join(word))