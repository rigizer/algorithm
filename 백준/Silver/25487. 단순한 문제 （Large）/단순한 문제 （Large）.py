import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    print(min(list(map(int, input().split()))))