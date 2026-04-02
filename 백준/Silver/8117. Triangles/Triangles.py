import sys

input_data = sys.stdin.read().split()
segment_lengths = []

for val in input_data:
    num = int(val)
    if num == 0:
        break
    segment_lengths.append(num)

segment_lengths.sort()
found_triangle = False

for idx in range(len(segment_lengths) - 2):
    if segment_lengths[idx] + segment_lengths[idx + 1] > segment_lengths[idx + 2]:
        print(segment_lengths[idx], segment_lengths[idx + 1], segment_lengths[idx + 2])
        found_triangle = True
        break

if not found_triangle:
    print('NIE')