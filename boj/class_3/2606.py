import sys
from collections import defaultdict
read = sys.stdin.readline

n = int(read())
v = int(read())
graph = defaultdict(list)
for _ in range(v):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

stack = [1]
visited = []
while stack:
    now = stack.pop()
    if now not in visited:
        visited.append(now)
        stack.extend(graph[now])
print(len(visited)-1)