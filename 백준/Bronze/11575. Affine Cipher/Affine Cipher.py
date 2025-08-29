import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = input()
    result.append(''.join([chr(((ord(i) - 65) * a + b) % 26 + 65) for i in s]))

print('\n'.join(result))