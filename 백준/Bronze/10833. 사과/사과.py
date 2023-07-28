n = int(input())
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    answer += b % a
    
print(answer)