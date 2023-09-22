scoreboard = input()
a = 0
b = 0;
 
for i in range(len(scoreboard)):
    if scoreboard[i] == 'A':
        a += int(scoreboard[i + 1])
    elif scoreboard[i] == 'B':
        b += int(scoreboard[i + 1])
 
print('A' if a > b else 'B')