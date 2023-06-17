while True:
    c_list = []
    n = input()
    
    if n == '0':
        break
    for i in n:
        c_list.append(i)

    t = 0
    for i in c_list:
        t += 1
        if i == '0':
            t += 4
        elif i == '1':
            t += 2
        else:
            t += 3
    t += 1
    print(t)