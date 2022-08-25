# 220825
# BOJ 11724번 연결 요소의 개수
# 분류: 그래프
# 난이도: 실버 2
# https://www.acmicpc.net/problem/11724
# 문제 풀이 핵심
# 모든 노드를 돌면서 dfs를 돌아주었음
# 이미 방문한 노드는 재방문하지 않음으로써 효율을 높였음

import sys
from collections import defaultdict, Counter
read = sys.stdin.readline

n, m = map(int, read().split())

# 그래프 생성
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

# 노드를 하나씩 돌면서 방문하지 않았던 노드들에 대해 dfs를 수행
visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
    stack = [i]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = i
            stack.extend(graph[node])

# 0번째 노드는 존재하지 않기 때문에 -1
print(len(Counter(visited))-1)