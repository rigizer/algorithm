n = int(input())
k = int(input())
arr = [input() for _ in range(n)]

check = [0] * n
temp = []

result = set()

def card(i):
    if i == k:
        result.add(''.join(temp))
        return

    for j in range(n):
        if check[j]: 
        	continue
        check[j] = 1
        temp.append(arr[j])

        card(i + 1)
        check[j] = 0
        temp.pop()
        
card(0)
print(len(result))