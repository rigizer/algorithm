upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

j, n = map(int, input().split())
ss = [input() for _ in range(n)]

result = 0
for s in ss:
    point = 0
    for i in s:
        if i in upper:
            point += 4
        elif i in lower:
            point += 2
        elif i in number:
            point += 2
        elif i == ' ':
            point += 1
    
    if point <= j:
        result += 1

print(result)