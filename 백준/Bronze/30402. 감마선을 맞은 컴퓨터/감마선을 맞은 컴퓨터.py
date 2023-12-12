photo = [list(map(str, input().split())) for _ in range(15)]

def check(photo):
    for i in range(15):
        for j in range(15):
            if photo[i][j] == 'w':
                return 'chunbae'
            elif photo[i][j] == 'b':
                return 'nabi'
            elif photo[i][j] == 'g':
                return 'yeongcheol'

print(check(photo))