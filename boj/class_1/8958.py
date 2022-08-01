for _ in range(int(input())):
    cnt, res = 0, []
    for c in input():
        if c == "O":
            cnt += 1
        else:
            cnt = 0
        res.append(cnt)
    print(sum(res))