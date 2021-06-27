n, room, cnt= int(input()), 1, 1
while True:
    if n <= room:
        print(cnt)
        break
    room += 6*cnt
    cnt += 1

