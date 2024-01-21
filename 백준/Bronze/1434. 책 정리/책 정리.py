n, m = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
print(sum(boxes) - sum(books))