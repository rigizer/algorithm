n = int(input())

found = False
result = []

for a in range(1, int(n ** 0.5) + 1):
    if n % a == 0:
        c = n // a
        for sign1 in [1, -1]:
            for sign2 in [1, -1]:
                aa = a * sign1
                cc = c * sign2
                target = -(n + 2)
                for b in range(-5000, 5001):
                    if b != 0 and target % b == 0:
                        d = target // b
                        if aa * d + b * cc == n + 1:
                            result = [aa, b, cc, d]
                            found = True
                            break
                if found:
                    break
            if found:
                break
    if found:
        break

if found:
    print(*result)
else:
    print(-1)