eratos = [True for _ in range(246913)]
for i in range(246913):
    if i == 0 or i == 1:
        eratos[i] = False
    else:
        if eratos[i]:
            for j in range(i+i, 246913, i):
                eratos[j] = False

while True:
    n = int(input())
    if not n: break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if eratos[i]: cnt += 1
    print(cnt)