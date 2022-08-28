# 220830
# BOJ 16928번 뱀과 사다리 게임
# 난이도: 골드 5
# https://www.acmicpc.net/problem/16928

''' 문제 풀이 핵심
1. 최단 경로 탐색은 BFS
2. visited를 만들어줘야 백트래킹이 헛돌지 않음 '''

import sys
from collections import deque
read = sys.stdin.readline

def bfs(snake):
    dq = deque([[1, 0]])
    visited = [0 for _ in range(101)]
    while dq:
        now, cnt = dq.popleft()
        if now == 100:
            return cnt
        if not visited[now]:
            visited[now] = 1
            for i in range(1, 7):
                try:
                    next = snake[now+i]
                except:
                    next = now+i
                dq.append([next, cnt+1])
            
if __name__ == "__main__":
    n, m = map(int, read().split())
    snake = dict()
    for _ in range(n+m):
        x, y = map(int, read().split())
        snake[x] = y
    res = bfs(snake)
    print(res)