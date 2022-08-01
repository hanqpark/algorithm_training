n, x = map(int, input().split())
for a in [i for i in list(map(int, input().split())) if i < x]:
    print(a, end=" ")
