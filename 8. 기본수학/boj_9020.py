import sys
read = sys.stdin.readline

eratos = [True for _ in range(10001)]
for i in range(10001):
    if i==0 or i==1: eratos[i] = False
    if eratos[i]:
        for j in range(i+i, 10001, i):
            eratos[j] = False

for _ in range(int(read())):
    n = int(read())
    minval = 1
    for i in range(2, n+1):
        if eratos[i] and eratos[n-i]:
            if n-i-i < 0: break
            if n-i-i < n-minval-minval: minval = i 
    print(minval, n-minval)

"""
eratos = [True for _ in range(10001)]
for i in range(2, 10001):
    if eratos[i]:
        for j in range(i+i, 10001, i):
            eratos[j] = False
sosu = [i for i in range(2, 10001) if eratos[i]]

for _ in range(int(read())):
    n = int(read())
    min_val = 0
    for s in sosu:
        if n-s in sosu:
            if abs(n-s-s) > abs(n-min_val-min_val): break
            min_val = s
    print(n-min_val, min_val)
"""