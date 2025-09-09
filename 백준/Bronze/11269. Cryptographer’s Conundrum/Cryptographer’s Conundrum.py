import sys
input = lambda: sys.stdin.readline().rstrip()

text = input()
pattern = 'PER' * (len(text) // 3)
result = 0

for i in range(len(text)):
    if text[i] != pattern[i]:
        result += 1

print(result)