for _ in range(int(input())):
    h, w, n = map(int, input().split())
    f = str(n%h) if n%h else str(h)
    back = n//h+1 if n%h else n//h
    b = '0'+str(back) if back < 10 else str(back)
    print(f+b)