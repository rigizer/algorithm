r, b = map(int,input().split())
size = r + b                      
i = 3                          
while True:                       
    if size % i == 0:            
        if (i - 2) * (size // i - 2) == b:   
            print(max(i, size // i), min(i, size // i))
            break
    i += 1