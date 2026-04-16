import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    while len(arr) > 2:
        i = 0
        j = len(arr) - 1
        new_arr = []
        
        while i <= j:
            if i == j:
                new_arr.append(arr[i] * 2)
            else:
                new_arr.append(arr[i] + arr[j])
            i += 1
            j -= 1
        
        arr = new_arr
    
    if arr[0] > arr[1]:
        result = 'Alice'
    else:
        result = 'Bob'
    
    print(f'Case #{tc}: {result}')