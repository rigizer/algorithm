a = 0
b = 0
apples = 0
for _ in range(int(input())):
    t, w, h, l = map(str, input().split())
    if t == 'A':
        apple = (int(w) // 12) * (int(h) // 12) * (int(l) // 12)
        a += apple * 500 + 1000
        apples += apple
    elif t == 'B':
        b += 6000
    
print(a + b)
print(apples * 4000)