import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
total = 0

while True:
    line = input()
    if not line:
        continue

    if line == '#':
        break

    if line == '0':
        result.append(str(total))
        total = 0
        continue

    parts = line.split()
    actual = int(parts[2])
    code = parts[3]

    if code == 'F':
        total += actual * 2
    elif code == 'B':
        total += actual + int(actual * 0.5 + 0.5)
    else:  # 'Y'
        total += 500 if actual < 500 else actual

print('\n'.join(result), end='')