import math
import sys
input = lambda: sys.stdin.readline().rstrip()

case = 1
result = []
while True:
    pizza_info = input()
    if pizza_info == '0':
        break
    r, w, l = map(int, pizza_info.split())
    diagonal = math.sqrt(w ** 2 + l ** 2)
    if diagonal <= 2 * r:
        result.append(f'Pizza {case} fits on the table.')
    else:
        result.append(f'Pizza {case} does not fit on the table.')
    case += 1

print('\n'.join(result))