# https://leetcode.com/problems/reconstruct-itinerary/

from collections import deque, defaultdict

def stack():
    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].popleft())
        route.append(stack.pop())
    return route[::-1]
        

def dfs(a):
    while graph[a]:
        dfs(graph[a].popleft())
    route.append(a)
    
    
if __name__ == "__main__":
    route = []
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # 그래프 생성
    graph = defaultdict(deque)
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    '''그래프 재귀 탐색
    dfs('JFK')
    print(route[::-1])'''
    
    # 그래프 stack 탐색
    print(stack())