n = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
result = 0

for n in nums:
    sum_nums -= n
    result += sum_nums * n

print(result)