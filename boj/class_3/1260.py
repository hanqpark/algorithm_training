import sys
from collections import defaultdict, deque
read = sys.stdin.readline


def dfs(g, v):
    stack = [v]
    way = []
    while stack:
        node = stack.pop()
        if node not in way:
            way.append(node)
            stack.extend(sorted(g[node], reverse=True))
    return way


def bfs(g, v):
    dq = deque([v])
    way = []
    while dq:
        node = dq.popleft()
        if node not in way:
            way.append(node)
            dq.extend(sorted(g[node]))
    return way


if __name__ == "__main__":
    n, m, v = map(int, read().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)
    print(*dfs(graph, v))
    print(*bfs(graph, v))