import sys
input = lambda: sys.stdin.readline().rstrip()

keypad = {
    'a': (2, 1), 'b': (2, 2), 'c': (2, 3),
    'd': (3, 1), 'e': (3, 2), 'f': (3, 3),
    'g': (4, 1), 'h': (4, 2), 'i': (4, 3),
    'j': (5, 1), 'k': (5, 2), 'l': (5, 3),
    'm': (6, 1), 'n': (6, 2), 'o': (6, 3),
    'p': (7, 1), 'q': (7, 2), 'r': (7, 3), 's': (7, 4),
    't': (8, 1), 'u': (8, 2), 'v': (8, 3),
    'w': (9, 1), 'x': (9, 2), 'y': (9, 3), 'z': (9, 4)
}

broken = list(map(int, input().split()))
text = input()

real_key = {}
for actual_key, original_key in enumerate(broken, start=1):
    real_key[original_key] = actual_key

result = []
prev_key = None

for ch in text:
    orig_key, count = keypad[ch]
    actual_key = real_key[orig_key]
    
    if prev_key == actual_key:
        result.append('#')
    result.append(str(actual_key) * count)
    prev_key = actual_key

print(''.join(result))