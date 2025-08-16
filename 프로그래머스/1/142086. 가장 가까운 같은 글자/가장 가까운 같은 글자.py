def solution(s):
    answer = []
    
    word = dict()
    for i, v in enumerate(s):
        before = word.get(v, -1)
        answer.append(-1 if before == -1 else i - before)
        word[v] = i
    
    return answer