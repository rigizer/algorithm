n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
p1, p2 = 0, n - 1

result = 0

while True:
    temp = nums[p1] + nums[p2]
    if temp == x:
        result += 1
        p2 -= 1
    elif temp < x:
        p1 += 1
    elif temp > x:
        p2 -= 1

    if p1 >= p2:
        break

print(result)