# 수열의 개수 n, 합이 m이어야 함
n, m = map(int, input().split())

# 수열
nums = list(map(int, input().split()))

# 시작 포인터 위치, 종료 포인터 위치
a, b = 0, 0

# 결과 저장
result = 0

while True:
    temp = 0
    for i in range(a, b + 1):
        temp += nums[i]
    
    if temp <= m:   # 같으면
        b += 1

        if temp == m:
            result += 1
    else:
        a += 1

    if b == n:
        break

print(result)