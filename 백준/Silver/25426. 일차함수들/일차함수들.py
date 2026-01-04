import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

a_list = []
b_sum = 0

for _ in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_sum += b

a_list.sort()

result = b_sum
for i in range(n):
    result += a_list[i] * (i + 1)

print(str(result))