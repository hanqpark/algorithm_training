from collections import defaultdict
from itertools import combinations

def solution(clothes):
    ans = 1
    kinds = [kind for cloth, kind in clothes]
    cnts = [kinds.count(kind) for kind in set(kinds)]
    for cnt in cnts:
        ans *= cnt+1
    return ans-1
    

def my_solution_failed(clothes):
    dic = defaultdict(list)
    for cloth, kind in clothes:
        dic[kind].append(cloth)
        
    ans = 0
    for i in range(1, len(dic)+1):
        comb = combinations(dic, i)
        for com in comb:
            tmp = 1
            for c in com:
                tmp *= len(dic[c])
            ans += tmp
    return ans
        