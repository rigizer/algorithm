burger = [int(input()) for _ in range(3)]
coke = int(input())
soda = int(input())
print(min(burger) + min(coke, soda) - 50)