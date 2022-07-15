from collections import deque

def iterative(start_v):
    discovered = [start_v]
    queue = deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
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
    res = iterative(1)
    print(res)