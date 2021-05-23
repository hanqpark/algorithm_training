'''셀프 넘버'''

con_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    con_num.add(i)

for i in range(1, 10001):
    if i not in con_num:
        print(i)


''' list 말고 set으로 해결하면 깔끔했다 '''