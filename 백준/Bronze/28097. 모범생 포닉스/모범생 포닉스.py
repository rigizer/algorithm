n = int(input())
time = sum([*map(int, input().split())]) + (n - 1) * 8
print(time // 24, time % 24)