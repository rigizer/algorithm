a, b, c = map(int, input().split())
t = int(input())

if t <= 30:
    result = a
else:
    extra_time = t - 30
    result = a + ((extra_time + b - 1) // b) * c

print(result)