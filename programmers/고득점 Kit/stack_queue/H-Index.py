
# 런타임 에러 솔루션
from collections import Counter
def solution(citations):
    hs = []
    n = len(citations)
    for c in citations:
        if c > n: continue
        if c == Counter(list(map(lambda x: x>=c, citations)))[True]:
            hs.append(c)
    return max(hs)
        