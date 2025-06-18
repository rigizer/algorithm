distance_history = map(int, input().split())

distance_list = [0]

for history in distance_history:
    distance_list.append(distance_list[-1] + history)

for i in range(5):
    relative_distance_list = []

    for j in range(5):
        city1 = distance_list[i]
        city2 = distance_list[j]

        relative_distance_list.append(max(city1, city2) - min(city1, city2))
    
    print(*relative_distance_list)