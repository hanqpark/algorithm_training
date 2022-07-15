# https://leetcode.com/problems/combinations/
import itertools
        
def combine(n: int, k: int):
    results = []
    
    def dfs(elements, start, k):
        if not k:
            results.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    
    dfs([], 1, k)
    return results

if __name__ == "__main__":
    n, k = 4, 2
    res = combine(n, k)
    print(res)
    
    print(list(itertools.combinations([i+1 for i in range(n)], k)))