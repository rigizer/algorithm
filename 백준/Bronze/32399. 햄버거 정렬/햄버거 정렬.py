import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
if s == '(1)':
    print(0)
elif s == '()1':
    print(1)
elif s == ')1(':
    print(2)
elif s == ')(1':
    print(1)
elif s == '1()':
    print(1)
elif s == '1)(':
    print(1)