tile = [0,1,3,5,11,21,43,85,171]
n = int(input())
if n < 9:
    print(tile[n])
else:
    for i in range(9, n+1):
        if (i-1)%2:
            tmp = tile[i-1]*2+1
        else:
            tmp = tile[i-1]*2-1
        tile.append(tmp%10007)
    print(tile[-1])