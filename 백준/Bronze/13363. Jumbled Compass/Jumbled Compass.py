import sys
input = lambda: sys.stdin.readline().rstrip()

n1 = int(input())
n2 = int(input())
diff = (n2 - n1) % 360
if diff > 180:
    diff -= 360
print(diff)