import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    total = 0
    for height in tree:
        if height > mid:
            total += height - mid
            if total >= m:
                break

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)