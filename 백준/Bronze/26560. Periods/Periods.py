n = int(input())
while True:
    try:
        s = input()
        if s[-1] == '.':
            print(s)
        else:
            print(s + '.')
    except:
        break