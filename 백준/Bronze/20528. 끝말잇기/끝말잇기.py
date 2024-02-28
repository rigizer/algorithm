n = int(input())
palindrome = input().split()
result = set()

for i in range(n) :
    result.add(palindrome[i][0])

if len(result) == 1 :
    print(1)
else :
    print(0)