def chicken_check(n, a, b, c):
    fried = a if a < n else n
    soy = b if b < n else n
    souce = c if c < n else n
    
    return fried + soy + souce

n = int(input())
a, b, c = map(int, input().split())

print(chicken_check(n, a, b, c))