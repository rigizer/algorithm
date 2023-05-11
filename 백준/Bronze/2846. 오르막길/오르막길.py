n = int(input())
board = list(map(int, input().split()))
a = 0
re = []

for i in range(n - 1):
    if board[i] < board[i + 1]:
        a += board[i + 1] - board[i]
    else:
        re.append(a)
        a = 0
        
re.append(a)
print(max(re))