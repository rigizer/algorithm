for _ in range(int(input())):
    school = [list(map(str, input().split())) for _ in range(int(input()))]
    school = sorted(school, key=lambda x:-int(x[1]))
    print(school[0][0])