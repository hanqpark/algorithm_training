for _ in range(int(input())):
    x, y = map(int, input().split()) # x, y값 받기
    dis = y-x # 실제 거리가 중요하므로 거리 계산하기
    idx = 0
    for i in range(pow(2, 31)):
        if dis < pow(i+1, 2):
            idx = i
            break
    # print(idx)
    dis -= idx*(idx+1)/2
    # dis -= sum([i+1 for i in range(idx)])

    cnt = idx
    while dis:
        if dis-idx < idx*(idx-1)/2:
            idx -= 1
        else:
            dis -= idx
            cnt += 1
            # print(f"dis:{dis}, cnt:{cnt}, idx:{idx}")
    print(cnt)


