while True:
    n = int(input())
    if n == 0:
        break
 
    arr = []
    for _ in range(n):
        word = input()
        arr.append(word)
 
    arr.sort(key=str.lower)
    print(arr[0])