import sys
read = sys.stdin.readline

n, m = map(int, read().split())
cards = list(map(int, read().split()))

maxval = 0
for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            temp = cards[x]+cards[y]+cards[z]
            if temp > maxval and temp <= m: maxval = temp
print(maxval)