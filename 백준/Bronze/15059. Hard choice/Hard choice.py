# 입력
available = list(map(int, input().split()))
needs = list(map(int, input().split()))

# 수요 예측
result = 0  # 못 먹는 사람 수
for i, j in zip(available, needs):
    if i - j < 0:
        result += (j - i)
print(result)