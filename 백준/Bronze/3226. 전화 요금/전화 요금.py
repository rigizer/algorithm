n = int(input())
result = 0

for _ in range(n):
    now, time = input().split()
    h, m = map(int, now.split(':'))
    current_time = h * 60 + m

    for i in range(int(time)):
        if current_time >= 420 and current_time < 1140:
            result += 10
            current_time += 1
        else:
            result += 5
            current_time += 1

        if current_time == 1440:
            current_time = 0

print(result)