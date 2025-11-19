tc = int(input())
for t in range(tc):
    a, b = map(int, input().split())
    x = a // b
    y = a % b
    print(f"#{t + 1} {x} {y}")