switch_count = int(input())                         
switch_state = list(map(int, input().split()))
switch_state.insert(0, 0)  
student_count = int(input())                     
student_switch = [list(map(int, input().split())) for _ in range(student_count)]

for gender, number in student_switch:
    if gender == 1:
        number_up = number
        while number_up < len(switch_state):
            switch_state[number_up] = 1 if switch_state[number_up] == 0 else 0
            number_up += number
    else:
        switch_state[number] = 1 if switch_state[number] == 0 else 0
        left = number - 1
        right = number + 1 
        while left > 0 and right < switch_count+1 and switch_state[left] == switch_state[right]:
            switch_state[left] = 1 if switch_state[left] == 0 else 0
            switch_state[right] = 1 if switch_state[right] == 0 else 0
            left -= 1
            right += 1

for num in range(1, len(switch_state)):
    print(switch_state[num], end = ' ')
    if num % 20 == 0:
        print()