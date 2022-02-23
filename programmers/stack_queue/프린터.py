from collections import deque
def solution(priorities, location):
    prior, locs, res = deque(priorities), deque([i for i in range(len(priorities))]), []
    while prior:
        p, l = prior.popleft(), locs.popleft()
        if prior:
            if p < max(prior): prior.append(p), locs.append(l)
            else: res.append(l)
        else: res.append(l); break
    return res.index(location)+1