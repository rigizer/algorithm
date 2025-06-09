n = int(input())
for _ in range(n):
    bef = input()
    aft = input()
    result = ''
    for ch in bef:
        if ch == ' ':
            result += ' '
        else:
            result += aft[ord(ch) - ord('A')]
    print(result)