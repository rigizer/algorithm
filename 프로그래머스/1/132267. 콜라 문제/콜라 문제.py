def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a:
            break
        i = (n // a) * b
        j = n % a
        answer += i
        n = i + j
    
    return answer