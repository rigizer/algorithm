n = int(input())
cost_list = []
for i in range(n) : 
    cost_list.append(int(input()))

m = int(input())
total_sum = 0
for i in range(m) : 
    total_sum += cost_list[int(input()) - 1]

print(total_sum)