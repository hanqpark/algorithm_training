# 220930
# 프로그래머스 43162번 네트워크
# 분류: 그래프
# 난이도: 레벨 3
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 한줄 평: 섬 찾는 문제 유형 많은데 오랜만에 풀려니 헤맸음..

from collections import defaultdict

def solution(n, computers):
    # 행렬을 Graph로 변환
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i is not j:
                if computers[i][j]:
                    graph[i].append(j)
    # DFS 실행
    islands, visited = 0, list()    # islands는 네트워크 그룹
    for i in range(n):              # 모든 노드를 돌며 네트워크 그룹을 탐색
        flag = False                # 이미 발견한 노드는 새로운 네트워크 그룹으로 취급 안함
        stack = [i]
        while stack:
            node = stack.pop()
            if node not in visited:
                flag = True         # 새로 발견한 노드는 새로운 네트워크 그룹으로 취급
                visited.append(node)
                stack.extend(graph[node])
        if flag:
            islands += 1
    return islands