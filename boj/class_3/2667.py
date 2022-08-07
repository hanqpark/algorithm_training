import sys
from collections import deque
# import pprint
# pp = pprint.PrettyPrinter()
read = sys.stdin.readline

n = int(read())
graph = [list(map(int, list(read().strip()))) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
danji = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] += 1
            dq = deque([[i, j]])
            cnt = 1
            while dq:
                y, x = dq.popleft()
                for xx, yy in zip(dx, dy):
                    newx, newy = xx+x, yy+y
                    if newx in range(0, n) and newy in range(0, n) and graph[newy][newx] == 1:
                        cnt += 1
                        graph[newy][newx] += 1
                        dq.append([newy, newx])
            danji.append(cnt)
# pp.pprint(graph)
danji.sort()
print(len(danji))
for d in danji:
    print(d)