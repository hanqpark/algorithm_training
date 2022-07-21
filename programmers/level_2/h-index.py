def solution(citations):
    for h in range(len(citations), -1, -1):
        if len([c for c in citations if c>=h]) >= h: return h