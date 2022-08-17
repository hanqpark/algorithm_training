# 2022.08.18
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기

from collections import defaultdict, deque

def solution(n, wires):
    ws = deque(wires)           # wires의 간선을 queue 형식으로 바꿔줌
    res = 101                   # n이 100이하인 자연수여서 최댓값을 101로 설정해줌
    # wires(ws)의 간선을 하나씩 빼면서 개수 차이 비교 실행
    for _ in range(n-1):                    
        tmp = ws.popleft()      # 간선을 왼쪽에서 하나 뺌
        # 트리 생성
        tree = defaultdict(list)            
        for w in ws:                        
            v1, v2 = w
            tree[v1].append(v2)
            tree[v2].append(v1)
        # DFS 실행
        stack, visited = [v1], set()        
        while stack:
            v = stack.pop()
            if v not in visited: 
                visited.add(v)
                stack.extend(tree[v])
        # 가장 차이가 적은 값 갱신
        vlen = len(visited)
        res = min(res, abs(n-vlen-vlen))   
        ws.append(tmp)          # 임시로 뺐던 간선을 다시 오른쪽에 삽입
    return res
            