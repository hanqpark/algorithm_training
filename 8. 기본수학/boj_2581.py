m = int(input())
n = int(input())
eratos = [1 for _ in range(n+1)]
for i in range(n):
    if i == 0 or i == 1:
        eratos[i] = 0
    else:
        if eratos[i]:
            for j in range(i+i, n+1, i):
                eratos[j] = 0

sosus = [i for i in range(m, n+1) if eratos[i]]
print(f"{sum(sosus)}\n{sosus[0]}" if sosus else -1)

