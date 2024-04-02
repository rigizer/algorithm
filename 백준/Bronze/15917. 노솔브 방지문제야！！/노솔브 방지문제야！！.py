import sys
for _ in range(int(input())):
    a = int(sys.stdin.readline())
    t = int(bin(a)[2:])
    print(1 if t & (-t) == a else 0)