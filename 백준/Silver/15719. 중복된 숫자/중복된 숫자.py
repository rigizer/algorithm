import sys
n = int(input())
sumN = sum(range(1, int(n)))
numbers = sys.stdin.readline().rstrip()
sumNum = 0
temp = ''
for num in numbers:
    if num.isdigit():
        temp += num
    else:
        sumNum += int(temp)
        temp = ''

sumNum += int(temp)

print(sumNum - sumN)