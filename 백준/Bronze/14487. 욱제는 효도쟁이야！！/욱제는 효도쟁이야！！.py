n = int(input())
town = list(map(int, input().split()))
print(sum(town) - max(town))