pizza = [int(input()) for _ in range(8)]
max_sum = 0
for i in range(8):
    total = 0
    for j in range(4):
        total += pizza[(i + j) % 8]
    max_sum = max(max_sum, total)
print(max_sum)