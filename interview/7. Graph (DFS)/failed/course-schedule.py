# https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque

def dfs(i):
    if i in traced: return False
    traced.add(i)
    for y in graph[i]:
        if not dfs(y): return False
    traced.remove(i)
    return True

if __name__ == "__main__":
    prerequisites = [[1,0],[0,1]]
    graph = defaultdict(deque)
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    flag = True
    for x in list(graph):
        if not dfs(x): 
            flag = False; break
            
    print(True)