n = int(input())
topping = input().split()
cheese = dict()

for t in topping:
    if t[-6::] == 'Cheese':
        cheese[t] = 1

print('yummy' if len(cheese.keys()) >= 4 else 'sad')