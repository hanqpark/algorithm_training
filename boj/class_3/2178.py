import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().strip())) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dq = deque([[0,0]])
while dq:
    x, y = dq.popleft()
    for xx, yy in zip(dx, dy):
        newx, newy = xx+x, yy+y
        if newx in range(0, m) and newy in range(0, n) and graph[newy][newx] == 1:
            graph[newy][newx] += graph[y][x]
            dq.append([newx,newy])
print(graph[-1][-1])