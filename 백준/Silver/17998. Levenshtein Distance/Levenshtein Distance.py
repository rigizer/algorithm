import sys
input = lambda: sys.stdin.readline().rstrip()

alphabet = input()
s = input()
result = set()
n = len(s)

for i in range(n):
    result.add(s[:i] + s[i+1:])
for i in range(n + 1):
    for c in alphabet:
        result.add(s[:i] + c + s[i:])
for i in range(n):
    for c in alphabet:
        if s[i] != c:
            result.add(s[:i] + c + s[i+1:])
if s in result:
    result.remove(s)
result = sorted(result)

for word in result:
    print(word)