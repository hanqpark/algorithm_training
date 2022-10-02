from itertools import permutations

n, m = map(int, input().split())
for p in permutations(list(i+1 for i in range(n)), m):
    print(" ".join(map(str, p)))