import sys
read = sys.stdin.readline

m, n = map(int, read().split())
pokemon = dict()
for i in range(1, m+1):
    p = read().strip()
    pokemon[p] = i
    pokemon[str(i)] = p

for _ in range(n):
    q = read().strip()
    print(pokemon[q])