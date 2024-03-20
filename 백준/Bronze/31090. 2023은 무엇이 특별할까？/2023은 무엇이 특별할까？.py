t = int(input())
for _ in range(t) : 
    year = input()
    num = year[2:4]
    
    print('Good' if (int(year) + 1) % int(num) == 0 else 'Bye')