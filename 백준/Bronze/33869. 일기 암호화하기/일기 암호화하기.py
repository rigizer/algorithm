import sys
input = lambda: sys.stdin.readline().rstrip()

w = input()
s = input()

seen = set()
key = []
for ch in w:
    if ch not in seen:
        seen.add(ch)
        key.append(ch)

alphabet = [chr(ord('A') + i) for i in range(26)]
cipher = key + [ch for ch in alphabet if ch not in seen]

mapping = {plain: cipher[i] for i, plain in enumerate(alphabet)}

result = ''.join(mapping[ch] for ch in s)
print(result)