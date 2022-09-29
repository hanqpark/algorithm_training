# 220929
# 프로그래머스 49189번 가장 먼 노드
# 분류: 그래프
# 난이도: 레벨 3
# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 한줄 평: 전형적인 BFS 문제를 살짝 꼬아놓은 느낌이지만 풀만했음

from collections import defaultdict, deque

def solution(n, edge):
    # 무향 그래프 생성
    graph = defaultdict(deque)
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    # BFS 실행
    far = defaultdict(set)      # 1번 노드와 현재 노드의 거리를 기록하는 Dict 
    visited = set()             # 방문한 노드는 처리 안하기 위해 check
    q = deque([[1, 0]])         # [루트노드 1, 거리(0) -> 자기 자신이므로]
    while q:
        node, cnt = q.popleft()
        if node not in visited:
            far[cnt].add(node)
            visited.add(node)
            for n in graph[node]:
                q.append([n, cnt+1])
    return len(far[max(far.keys())])    # 가장 먼 거리의 node의 수를 반환
