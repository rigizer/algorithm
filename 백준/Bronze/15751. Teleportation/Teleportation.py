a, b, x, y = map(int, input().split())
a, b = min(a, b), max(a, b)
x, y = min(x, y), max(x, y) 
distance = b - a 
teleporter = abs(x - a) + abs(y - b)
result = min(distance, teleporter)
print(result)