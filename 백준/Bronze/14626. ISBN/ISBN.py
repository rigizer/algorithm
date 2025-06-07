isbn = input()
result = 0
is_even = False
for i in range(13):
    if isbn[i] == '*':
        if i % 2 != 0:
            is_even = True
        continue
    result += int(isbn[i]) * (1 if i % 2 == 0 else 3)

if is_even == True:
    for i in range(10):
        if (result + (i * 3)) % 10 == 0:
            print(i)
            break
else:
    print(10 - result % 10)