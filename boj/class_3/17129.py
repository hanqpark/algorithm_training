import sys
from collections import defaultdict
read = sys.stdin.readline

m, n = map(int, read().split())
dic = defaultdict(str)
for _ in range(m):
    site, pswd = read().split()
    dic[site] = pswd

for _ in range(n):
    print(dic[read().strip()])
