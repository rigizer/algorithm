n = int(input())
nums = list(map(int, input().split()))
ans, benefit = 0, 0
 
for i in range(len(nums)-1, -1, -1):
    benefit = max(benefit, nums[i])
    ans = max(ans, benefit - nums[i])

print(ans)