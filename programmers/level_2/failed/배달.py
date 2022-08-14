import heapq
from collections import defaultdict


def dijkstra(graph, root):
    weights = {node: float('inf') for node in graph}  # root로 부터의 거리 값을 저장하기 위함
    weights[root] = 0  # 시작 값은 0이어야 함
    heap = []
    heapq.heappush(heap, [weights[root], root])  # 시작 노드부터 탐색 시작 하기 위함. [weight, root]

    while heap:  # heap에 남아 있는 노드가 없으면 끝
        weight, node = heapq.heappop(heap)  # 탐색 할 노드, 거리를 가져옴.
        if weights[node] < weight:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        for next_node, next_weight in graph[node].items():
            dist = weight + next_weight  # 해당 노드를 거쳐 갈 때 거리
            if dist < weights[next_node]:  # 알고 있는 거리 보다 작으면 갱신
                weights[next_node] = dist
                heapq.heappush(heap, [dist, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return weights  


def solution(N, road, K):
    graph = defaultdict(dict)
    for r in road:
        u, v, w = r
        try:
            if graph[u][v] < w: continue
        except:
            pass
        graph[u][v] = w
        graph[v][u] = w
    res = dijkstra(graph, 1)
    return sum(1 for v in res.values() if v <= K)


road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
print(solution(6, road, 4))