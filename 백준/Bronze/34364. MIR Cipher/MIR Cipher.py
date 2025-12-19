import sys
input = lambda: sys.stdin.readline().rstrip()

n, s = input().split()
n = int(n)

result = []
shift = 1

for ch in s:
    value = ord(ch) - ord('A')
    new_value = (value + shift) % 26
    result.append(chr(new_value + ord('A')))
    shift = (shift * 2) % 26

sys.stdout.write(''.join(result))