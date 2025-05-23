n = int(input())
a = list(map(int,input().split()))

battery = 2
percent = 2 

for i in range(n - 1):
    if a[i] == a[i + 1]:
        percent *= 2
        battery += percent
        if battery >= 100:
            battery = 0
            percent = 1
    else:
        battery += 2
        percent = 2
        if battery >= 100:
            battery = 0
            percent = 1
print(battery)