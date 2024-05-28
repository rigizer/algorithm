w = input()
a = [0] * 10
for i in range(len(w)):
    n = int(w[i])
    if n == 6 or n == 9:
        if a[6] <= a[9]:
            a[6] += 1
        else:
            a[9] += 1
    else:
        a[n] += 1
 
print(max(a))