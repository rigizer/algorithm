n = int(input())
 
arr1 = []
arr2 = []
 
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    arr1.append([yyyy, mm, dd, name])
    arr2.append([yyyy, mm, dd, name])

arr1.sort()
arr2.sort(reverse=True)
 
print(arr2[0][3])
print(arr1[0][3])