# 2022.08.19
# https://www.acmicpc.net/problem/1697
# 숨바꼭질
''' 도움 받은 사이트
https://www.acmicpc.net/board/view/88502 <- 반례 모음 '''

from collections import deque

def main():
    n, k = map(int, input().split())
    # mini, maxi = min(n, k), max(n, k)         n, k가 바뀌어도 상관 없을 줄 알았는데 나누기 2는 없다는 것을 잊었음 -> 반례: 100 0 = 100
    q = deque([[n, 0]])                         # BFS로 풀었음
    visited = [0 for _ in range(100001)]        # 방문한 애들을 또 방문하는 것은 시간상, 메모리상 손해가 너무 큼
    while q:
        now, cnt = q.popleft()
        if now < 0 or now > 100000 or visited[now]:     # 범위 벗어나거나 이미 방문한 애들은 continue
            continue
        if now == k:        
            return cnt
        visited[now] = 1
        q.append([now*2, cnt+1])
        q.append([now+1, cnt+1])
        q.append([now-1, cnt+1])


if __name__ == "__main__":
    res = main()
    print(res)
