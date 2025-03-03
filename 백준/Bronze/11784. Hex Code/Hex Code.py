while True:
    try:
        data = input()
        print(''.join([chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2)]))

    except:
        break