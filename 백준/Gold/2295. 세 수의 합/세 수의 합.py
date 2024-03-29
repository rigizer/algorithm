n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
flag = True
result = 0
while flag:
    num = nums.pop()
    for i in range(len(nums)):
        left = i
        right = len(nums) - 1
        while left <= right:
            temp = nums[i] + nums[left] + nums[right]
            if temp < num:
                left += 1
            elif temp > num:
                right -= 1
            else:
                result = num
                flag = False
                break
print(result)