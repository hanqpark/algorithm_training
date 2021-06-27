from math import sqrt
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    centers = sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
    rs = r1+r2
    if 

    if centers < rs: print(0 if x1==x2 and y1==y2 else 2)
    elif centers == rs: print(-1 if x1==x2 and y1==y2 else 1)
    elif centers > rs: print(0)


