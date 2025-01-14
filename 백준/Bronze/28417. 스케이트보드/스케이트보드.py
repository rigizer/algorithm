N = int(input())
maxNum = 0
for i in range(N) : 
    inputList = list(map(int, input().split()))
    sum = 0
    aList = []
    bList = []
    
    for j in range(0,2) : 
        aList.append(int(inputList[j]))
    
    for j in range(2,7) : 
        bList.append(int(inputList[j]))
    
    aList.sort()
    bList.sort()
    
    sum += aList[1] + bList[3] + bList[4]
    
    maxNum = max(maxNum, sum)

print(maxNum)