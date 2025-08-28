while True:
    words = input().split()
    if words[0] == '#':
        break
    print(' '.join([i[::-1] for i in words]))