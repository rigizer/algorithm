from collections import deque

def min_operations(start, target):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        if current in visited:
            continue
        visited.add(current)

        if len(current) > 1:
            for i in range(1, len(current)):
                flipped = current[:i] + ('1' if current[i] == '0' else '0') + current[i+1:]
                queue.append((flipped, steps + 1))

        plus_one = bin(int(current, 2) + 1)[2:]
        queue.append((plus_one, steps + 1))

        if int(current, 2) > 0:
            minus_one = bin(int(current, 2) - 1)[2:]
            queue.append((minus_one, steps + 1))

    return -1

start = input()
target = input()

print(min_operations(start, target))