alpah = {'A': 3, 'B': 2, 'C' : 1, 'D' : 2, 'E' : 3, 'F' : 3, 'G' : 2, 
         'H' : 3, 'I' : 3, 'J' : 2, 'K' : 2, 'L' : 1, 'M' : 2, 'N' : 2, 
         'O': 1, 'P' : 2, 'Q': 2, 'R': 2, 'S' : 1, 'T' : 2, 'U': 1, 'V' : 1, 
         'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1}
man = input()
woman = input()
lst = []
for i in range(len(man)):
    lst.append(man[i])
    lst.append(woman[i])
for i in range(len(lst)):
    lst[i] = str(alpah[lst[i]])
while True:
    for i in range(len(lst)-1):
        lst[i] = str((int(lst[i]) + int(lst[i+1])) % 10)
    lst.pop()
    if len(lst) == 2:
        for i in lst:
            print(int(i), end='')
        break