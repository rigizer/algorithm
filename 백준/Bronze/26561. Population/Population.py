def population(begin_num, time):
    plus_num = time // 4
    minus_num = time // 7
    return begin_num + plus_num - minus_num

if __name__ == '__main__':
    for _ in range(int(input())):
        begin_num, time = map(int, input().split())
        print(population(begin_num, time))