def solution(k, score):
    answer = []
    m = []
    for i in score:
        m.append(i)
        if len(m) > k:
            m.remove(min(m))
        answer.append(min(m))
    return answer