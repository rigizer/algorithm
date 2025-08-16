def solution(s):
    answer = 0
    x = None
    x_cnt = 0
    non_x_cnt = 0

    for i, v in enumerate(s):
        if x is None:
            x = v
            x_cnt = 1
            non_x_cnt = 0
        else:
            if v == x:
                x_cnt += 1
            else:
                non_x_cnt += 1

        if x_cnt == non_x_cnt:
            answer += 1
            x = None
            x_cnt = 0
            non_x_cnt = 0

    if x is not None:
        answer += 1

    return answer