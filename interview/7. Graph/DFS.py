# DFS 기본 코드

# 왼쪽 우선 탐색 (재귀 구조이기 때문에)
def recursive(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive(w, discovered)
    return discovered

# 오른쪽 우선 탐색 (Stack이기 때문에)
def iterative(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


if __name__ == "__main__":
    graph = {
        1: [2,3,4],
        2: [5],
        3: [5],
        4: [],
        5: [6,7],
        6: [],
        7: [3],
    }
    res = recursive(1)
    print(res)