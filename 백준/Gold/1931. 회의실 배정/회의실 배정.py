import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

result = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        result += 1
        end_time = end

print(result)