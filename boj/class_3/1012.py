import sys
from collections import deque
read = sys.stdin.readline

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for _ in range(int(read())):
    m, n, k = map(int, read().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, read().split())
        graph[y][x] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                graph[i][j] += 1
                dq = deque([[i, j]])
                while dq:
                    y, x = dq.popleft()
                    for xx, yy in zip(dx, dy):
                        newx, newy = xx+x, yy+y
                        if newx in range(0, m) and newy in range(0, n) and graph[newy][newx] == 1:
                            graph[newy][newx] += 1
                            dq.append([newy, newx])
    print(cnt)