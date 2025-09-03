import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
base = input()
words = [input() for _ in range(n - 1)]

def get_count(word):
    count = [0] * 26
    for c in word:
        count[ord(c) - 65] += 1
    return count

base_count = get_count(base)
result = 0

for word in words:
    word_count = get_count(word)
    diff = 0

    for i in range(26):
        diff += abs(base_count[i] - word_count[i])

    if diff == 0:
        result += 1
    elif diff == 1:
        result += 1
    elif diff == 2 and len(base) == len(word):
        result += 1

print(result)