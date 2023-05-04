def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    a_idx = 0
    b_idx = 0
    while b_idx < len(B):
        if B[b_idx] > A[a_idx]:
            answer += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1

    return answer