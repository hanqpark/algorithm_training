# https://leetcode.com/problems/assign-cookies/

from bisect import bisect_right

def sol(g, s):
    g.sort()
    s.sort()
    ans = []
    while g and s:
        greed = g.pop()
        size = s.pop()
        if size < greed:
            s.append(size)
        else:
            ans.append(greed)
    return len(ans)


def bisect_sol(g, s):
    g.sort()
    s.sort()
    
    res = 0
    for i in s:
        idx = bisect_right(g, i)
        if idx > res:
            res += 1
    return res