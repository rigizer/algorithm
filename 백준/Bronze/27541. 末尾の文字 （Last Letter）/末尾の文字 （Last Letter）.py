n = int(input())
s = input()

if s[-1] == 'G':
    print(s[:n - 1])
else:
    print(s + 'G')