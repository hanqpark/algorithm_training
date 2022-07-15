# https://leetcode.com/problems/permutations/

import itertools

def dfs(elements):
    if len(elements)==0:
        results.append(prev_elements[:])
    
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)
        
        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()


if __name__ == "__main__":
    results = []
    prev_elements = []
    nums = [1,2,3]
    dfs(nums)
    print(results)
    
    print(list(map(list, itertools.permutations(nums))))
            