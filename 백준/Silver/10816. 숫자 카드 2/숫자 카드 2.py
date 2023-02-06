n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

dict = {}

# dictonary의 key 생성
for i in range(m):
    dict[m_num[i]] = 0

# n_num 탐색 및 숫자 카드 정수 확인
for i in range(n):
    if dict.get(n_num[i]) != None:
        dict[n_num[i]] += 1

# 데이터 출력
for i in range(m):
    print(dict.get(m_num[i]), end=' ')