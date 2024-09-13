for _ in range(int(input())):
    name = list(input().split())
    name.pop(0)
    name.insert(0, 'god')
    print(''.join(name))