import sys
read = sys.stdin.readline

n, m = map(int, read().split())
d = set(read().strip() for _ in range(n))
b = set(read().strip() for _ in range(n))
res = d-(d-b)
res = sorted(list(res))
print(len(res))
for r in res:
    print(r)
