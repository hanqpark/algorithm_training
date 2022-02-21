'''그룹 단어 체커'''
cnt = 0
for _ in range(int(input())):
    ss = input()
    arr = []
    flag = True
    for s in ss:
        if s in arr and s != arr[-1]:
            flag = False
            break
        arr.append(s)
    if flag:
        cnt += 1
print(cnt)