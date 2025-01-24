t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    a.pop(0)
    a.sort(reverse=True)
    value = []
    for j in range(1, len(a)):
        value.append(a[j-1]-a[j]) 
    print(f'Class {i+1}')
    print(f'Max {max(a)}, Min {min(a)}, Largest gap {max(value)}')