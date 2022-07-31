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


def sangyun(maps):    
    dx=[-1,1,0,0] # 움직일 방향 설정
    dy=[0,0,-1,1]
    n=len(maps)-1
    m=len(maps[0])-1

    def bfs(x,y):
        queue=deque([])
        queue.append([x,y])
        
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if nx<0 or nx>n or ny<0 or ny>m: # 못가는 길이라면 continue
                    continue
                elif maps[nx][ny]==0: # 막힌 길이라면 continue
                    continue
                elif maps[nx][ny]==1: # 갈 수 있는 길이라면, 여태껏 걸은 칸+1 을 더해줌
                    if nx!=0 or ny!=0:
                        maps[nx][ny]=maps[x][y]+1
                        queue.append([nx,ny])
            
                if nx==n and ny==m:
                    if maps[nx][ny]!=0 or maps[nx][ny]!=1:
                        return maps[nx][ny]
                    
                    return -1
    return bfs(0,0)
    

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    res = sangyun(maps)
    print(res)