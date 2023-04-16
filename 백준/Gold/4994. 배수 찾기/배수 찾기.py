def find(n):
    list = ['']
    while True:
        for m in list:
            for i in range(2):
                num = m + str(i)

                if int(num) != 0 and int(num) % n == 0:
                    return num
                
                list.append(num)

while True:
    n = int(input())

    if n == 0:
        break
    
    result = find(n)
    print(result)