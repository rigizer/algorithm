n, b = input().split(' ')
n = ''.join(reversed(n))
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0 

for x in range(len(n) - 1, -1, -1):
	sum = number.index(n[x]) * (b ** x)
	result += sum
    
print(result)