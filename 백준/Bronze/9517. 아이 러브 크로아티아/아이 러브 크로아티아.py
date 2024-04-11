k = int(input())
lst = [input() for _ in range(int(input()))]
time = 0
for i in lst :
    t, z = i.split()
    if z == 'T' :
        if time + int(t) < 210 :
            time += int(t)
            k += 1
            if k == 9:
                k = 1
        else:
            print(k)
            break
    else :
        time += int(t)
        if time >= 210 :
            print(k)
            break