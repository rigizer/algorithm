import sys
input = lambda: sys.stdin.readline().rstrip()

a = input()
b = input()

print(a)
print(b)

x = int(a)
y = b[::-1]

for d in y:
    print(x * int(d))

result = x * int(b)
print(result)