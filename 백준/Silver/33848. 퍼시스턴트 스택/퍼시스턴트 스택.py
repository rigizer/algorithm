import sys
input = lambda: sys.stdin.readline().rstrip()

input_data = sys.stdin.read().split()
ptr = 0

q = int(input_data[ptr])
ptr += 1

states = [(-1, 0, 0)]
result = []

for _ in range(q):
    t = input_data[ptr]
    ptr += 1

    if t == '1':
        x = int(input_data[ptr])
        ptr += 1
        states.append((x, states[-1][1] + 1, len(states) - 1))

    elif t == '2':
        states.append(states[states[-1][2]])

    elif t == '3':
        k = int(input_data[ptr])
        ptr += 1
        states = states[:len(states) - k]

    elif t == '4':
        result.append(str(states[-1][1]))

    elif t == '5':
        result.append(str(states[-1][0]))

print('\n'.join(result))