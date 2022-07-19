# https://leetcode.com/problems/minimum-height-trees/

from mailcap import findmatch
from typing import List
from collections import defaultdict


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n<=1: return [0]
    
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)
    
    while n>2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor])==1:
                new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves
            
            
if __name__ == "__main__":
    edges = [[1,3], [2,3], [3,4], [3,5], [4,6], [6,10], [5,7], [5,8], [8,9]]
    res = findMinHeightTrees(10, edges)
    print(res)