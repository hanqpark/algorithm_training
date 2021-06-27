for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(n%h*100 + n//h + 1 if n%h else h*100 + n//h)