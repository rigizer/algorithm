a, b = map(int, input().split())
c = int(input())
print(a + b - 2 * c if a + b >= 2 * c else a + b)