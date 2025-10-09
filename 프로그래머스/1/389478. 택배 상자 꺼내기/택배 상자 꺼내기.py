def get_answer(q, w, num, box):
    for i in range(q):
        for j in range(w):
            if box[i][j] == num:
                count = 0
                for x in range(i, q):
                    if box[x][j] == -1:
                        break
                    count += 1
                return count
    return 0

def solution(n, w, num):
    if n % w == 0:
        q = n // w
    else:
        q = (n // w) + 1

    box = [[-1] * w for _ in range(q)]

    x = 1
    done = False
    for i in range(q):
        if i % 2 == 0:
            for j in range(w):
                if x > n:
                    done = True
                    break
                box[i][j] = x
                x += 1
        else:
            for j in range(w - 1, -1, -1):
                if x > n:
                    done = True
                    break
                box[i][j] = x
                x += 1
        if done:
            break

    answer = get_answer(q, w, num, box)
    return answer