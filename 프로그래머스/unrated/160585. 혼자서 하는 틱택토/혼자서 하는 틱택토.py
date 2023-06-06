# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 혼자서 하는 틱택토

# 혼자서 게임을 진행
# O, X를 혼자서 번갈아가면서 진행
# 틱택토를 진행하면서 나올 수 있는 게임 상황이면 1
# 그렇지 않으면 0을 return하는 함수 작성

# 실수 case 1: O을 표시할 차례인데 X 표시
# 실수 case 2: 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다

BOARD_SIZE = 3

def solution(board):
    # O와 X의 전체 갯수 확인
    o_cnt = 0
    x_cnt = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 'O':
                o_cnt += 1
            if board[i][j] == 'X':
                x_cnt += 1

    # O보다 X 갯수가 더 큰 경우 확인 (같거나, 한 개만 차이나야 함)
    if o_cnt < x_cnt:
        return 0
    
    # O가 X보다 1개보다 더 차이나는 경우 확인 (O만 너무 많이 그리면 안 됨)
    if o_cnt - x_cnt > 1:
        return 0

    # 가로, 세로 탐색
    for i in range(BOARD_SIZE):
        o_win_garo = 0
        o_win_sero = 0
        x_win_garo = 0
        x_win_sero = 0
        for j in range(BOARD_SIZE):
            if board[i][j] == 'O':
                o_win_garo += 1
            if board[j][i] == 'O':
                o_win_sero += 1
            if board[i][j] == 'X':
                x_win_garo += 1
            if board[j][i] == 'X':
                x_win_sero += 1
        
        # O가 이겼는지 확인
        if o_win_garo == 3 or o_win_sero == 3:
            # O가 이기기 위해서는 항상 X보다 1개 더 많은 상태여야 하는데, 그렇지 않은 경우 확인
            if o_cnt <= x_cnt:
                return 0
        
        # X가 이겼는지 확인
        if x_win_garo == 3 or x_win_sero == 3:
            # X가 이기기 위해서는 항상 O와 같은 갯수의 상태여야 하는데, 그렇지 않은 경우 확인
            if o_cnt != x_cnt:
                return 0
    
    # 대각선 탐색 (좌상 -> 우하)
    if (board[0][0], board[1][1], board[2][2]) == ('O', 'O', 'O'):
        if o_cnt <= x_cnt:
            return 0
    
    if (board[0][0], board[1][1], board[2][2]) == ('X', 'X', 'X'):
        if o_cnt != x_cnt:
            return 0

    # 대각선 탐색 (좌하 -> 우상)
    if (board[0][2], board[1][1], board[2][0]) == ('O', 'O', 'O'):
        if o_cnt <= x_cnt:
            return 0

    
    if (board[0][2], board[1][1], board[2][0]) == ('X', 'X', 'X'):
        if o_cnt != x_cnt:
            return 0

    return 1