import sys
input = lambda: sys.stdin.readline().rstrip()

d = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(360, d)
answer = 360 // g

print(str(answer))