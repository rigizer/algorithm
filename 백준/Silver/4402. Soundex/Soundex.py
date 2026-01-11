import sys
input = lambda: sys.stdin.readline().rstrip()

mapping = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}

for line in sys.stdin:
    word = line.rstrip()
    if not word:
        continue

    result = []
    prev = ''

    for ch in word:
        code = mapping.get(ch, '')
        if code != prev:
            if code:
                result.append(code)
            prev = code
        else:
            prev = code

    print(''.join(result))