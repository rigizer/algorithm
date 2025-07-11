n = int(input())
for _ in range(n):
    sentence = input().lower()
    appeared = set(c for c in sentence if 'a' <= c <= 'z')
    missing = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in appeared]
    if not missing:
        print('pangram')
    else:
        print('missing', ''.join(missing))