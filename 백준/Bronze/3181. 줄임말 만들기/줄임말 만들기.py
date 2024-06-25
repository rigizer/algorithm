a = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
b = input().split()
r = b[0][0]

for i in range(1,len(b)):
    if b[i] in a:
        continue
    r += b[i][0]
print(r.upper())