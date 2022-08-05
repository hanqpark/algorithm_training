from sys import stdin
read = stdin.readline
for x, y in sorted(list(map(int, read().split())) for _ in range(int(read()))):
    print(x, y)