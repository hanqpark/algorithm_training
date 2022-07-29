'''
    공간 복잡도를 더 잡아먹는 방법(graph = [])이 있고,
    시간 복잡도를 더 잡아먹는 방법(map에 count를 늘려주는 방법)이 있다.
    속도는 당연히 공간복잡도를 더 잡아먹는 방법이 월등히 빠르다...
'''

from collections import deque

# 단순히 visited에 1을 추가해서 이미 방문했던 곳이면 return을 해주는 방식이었음 -> 다른 짧은 경로에 대해 거절을 때려버리는 단점이 존재함
def mysol(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    xx, yy = len(maps[0])-1, len(maps)-1
    
    def dfs(y, x):
        if x<0 or y<0 or x>xx or y>yy or maps[y][x] == 0 or visited[y][x] == 1 or visited[yy][xx] == 1:
            return

        visited[y][x] = 1
        dfs(y+1, x)
        dfs(y, x+1)
        dfs(y-1, x)
        dfs(y, x-1)
    
    dfs(0, 0)
    return sum([sum(v) for v in visited]) if visited[yy][xx] else -1


def bfs_sol(maps):
    row_len, col_len = len(maps[0])-1, len(maps)-1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    dq = deque([[0,0,1]])
    
    while dq:
        x, y, cnt = dq.popleft()
        maps[y][x] += cnt
        if (x, y) == (row_len, col_len): break
        for a, b in zip(dx, dy):
            if x+a<0 or y+b<0 or x+a>row_len or y+b>col_len or maps[y+b][x+a]==0 or (maps[y+b][x+a] != 1 and maps[y+b][x+a] < cnt+1):
                continue
            dq.append([x+a, y+b, cnt+1])
    goal = maps[col_len][row_len]-1
    return goal if goal else -1


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    answer = graph[-1][-1]
    return answer