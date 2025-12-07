import sys
input = lambda: sys.stdin.readline().rstrip()

mapping = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}

t = int(input())

for i in range(t):
    raw = input()
    digits = []

    for ch in raw:
        if ch.isdigit():
            digits.append(ch)
        elif ch.isalpha():
            digits.append(mapping[ch.upper()])
        if len(digits) == 10:
            break

    phone = ''.join(digits)
    result = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
    if i == t - 1:
        print(result)
    else:
        print(result)