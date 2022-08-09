import sys
from collections import defaultdict, deque
read = sys.stdin.readline

g = defaultdict(list)
n = int(read())
for i in range(n):
    for j, x in enumerate(list(map(int, read().split()))):
        if x: g[i].append(j)

for i in range(n):
    dq = deque([i])
    visited = []
    res = []
    flag = False
    while dq:
        now = dq.popleft()
        if now not in visited:
            if flag:
                visited.append(now)
            flag = True
            dq.extend(g[now])
    for j in range(n):
        tmp = 1 if j in visited else 0
        res.append(tmp) 
    print(" ".join(map(str, res)))
        