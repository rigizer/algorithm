import sys
input = lambda: sys.stdin.readline().rstrip()

def check_line(table):
    for i in range(9):
        check = [False] * 10
        for j in range(9):
            if check[table[i][j]] == True:
                return False
            check[table[i][j]] = True
    
    return True

def check_group(table):
    for i in range(3):
        for j in range(3):
            check = [False] * 10
            for k in range(3):
                for l in range(3):
                    if check[table[i * 3 + k][j * 3 + l]] == True:
                        return False
                    check[table[i * 3 + k][j * 3 + l]] = True
    
    return True

n = int(input())
result = []
for i in range(n):
    table = [list(map(int, input().split())) for _ in range(9)]
    if i < n - 1:
        input()
    
    garo = check_line(table)
    if not garo:
        result.append(f"Case {i + 1}: INCORRECT")
        continue
    
    sero = check_line(list(zip(*table)))
    if not sero:
        result.append(f"Case {i + 1}: INCORRECT")
        continue
    
    group = check_group(table)
    if not group:
        result.append(f"Case {i + 1}: INCORRECT")
        continue
    
    result.append(f"Case {i + 1}: CORRECT")
    
print('\n'.join(result))