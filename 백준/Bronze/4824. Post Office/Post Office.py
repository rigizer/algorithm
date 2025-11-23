import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    a, b, c = map(float, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    dims = sorted([a, b, c])
    thickness = dims[0]
    height = dims[1]
    length = dims[2]

    if 125 <= length <= 290 and 90 <= height <= 155 and 0.25 <= thickness <= 7:
        print('letter')
        continue

    letter_min_ok = (length >= 125 and height >= 90 and thickness >= 0.25)
    letter_max_exceed = (length > 290 or height > 155 or thickness > 7)

    if letter_min_ok and letter_max_exceed:
        if length <= 380 and height <= 300 and thickness <= 50:
            print('packet')
            continue

    packet_max_exceed = (length > 380 or height > 300 or thickness > 50)
    if letter_min_ok and packet_max_exceed:
        girth = 2 * (height + thickness)
        if length + girth <= 2100:
            print('parcel')
            continue

    print('not mailable')