# 유형: BFS
# 제목: 특정 거리의 도시 찾기
# 번호: 18352
# 난도: 실버 2
# 일자: 2023년 5월 5일 금요일
# 링크: https://www.acmicpc.net/problem/18352

# 틀린 이유: 문제를 똑바로 읽자.. (오름차순 출력)
# 오답 참고: https://steadily-worked.tistory.com/646

import sys
from collections import defaultdict, deque

read = sys.stdin.readline

if __name__ == "__main__":
    n, m, k, x = map(int, read().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a].append(b)
    
    visited = defaultdict(int)
    answer = list()
    dq = deque([[x, 0]])
    while dq:
        city, cnt = dq.popleft()
        if city not in visited.keys():
            visited[city] = cnt
            if cnt == k: answer.append(city)
            for g in graph[city]:
                dq.append([g, cnt+1])
    
    res = -1 if not answer else "\n".join(map(str, sorted(answer)))
    print(res)