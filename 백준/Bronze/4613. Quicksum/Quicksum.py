import sys
input = lambda: sys.stdin.readline().rstrip()

answer = []
while True:
    line = input().rstrip()
    if line == '#':
        break
    
    result = 0
    for idx, ch in enumerate(line, start=1):
        if ch != ' ':
            value = ord(ch) - ord('A') + 1
            result += idx * value
    answer.append(str(result))

print('\n'.join(answer))