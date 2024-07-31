def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if isPrime(num):
            print(num)
            break
        num += 1