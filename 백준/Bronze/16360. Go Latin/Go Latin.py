n = int(input())

for _ in range(n):
    word = input()
    if word.endswith('a'):
        result = word[:-1] + 'as'
    elif word.endswith('i') or word.endswith('y'):
        result = word[:-1] + 'ios'
    elif word.endswith('l'):
        result = word[:-1] + 'les'
    elif word.endswith('n'):
        result = word[:-1] + 'anes'
    elif word.endswith('ne'):
        result = word[:-2] + 'anes'
    elif word.endswith('o'):
        result = word[:-1] + 'os'
    elif word.endswith('r'):
        result = word[:-1] + 'res'
    elif word.endswith('t'):
        result = word[:-1] + 'tas'
    elif word.endswith('u'):
        result = word[:-1] + 'us'
    elif word.endswith('v'):
        result = word[:-1] + 'ves'
    elif word.endswith('w'):
        result = word[:-1] + 'was'
    else:
        result = word + 'us'
    print(result)