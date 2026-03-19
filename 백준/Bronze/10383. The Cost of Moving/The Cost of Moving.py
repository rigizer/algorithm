import sys
input = lambda: sys.stdin.readline().rstrip()

site = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = []
    
    while len(arr) < n:
        arr += input().split()
    
    sorted_arr = sorted(arr)
    
    pos = {}
    
    for i in range(n):
        pos[sorted_arr[i]] = i
    
    result = 0
    
    for i in range(n):
        result += abs(i - pos[arr[i]])
    
    print(f'Site {site}: {result}')
    
    site += 1