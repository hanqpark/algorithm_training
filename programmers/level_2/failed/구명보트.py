# Greedy는 무조건 정렬!!!!!!!!!!!!!!!

from collections import Counter, deque

def solution(people, limit):
    people.sort()
    p = deque(people)
    cnt = 0
    while p:
        front = p.popleft()
        cnt += 1
        while p and front+p[-1] > limit:
            p.pop()
            cnt += 1
        if p: p.pop()
    return cnt

def second(people, limit):
    p = Counter(people)
    cnt = 0
    keys = sorted(p.keys(), reverse=True)
    
    for k, v in p.items():
        if not p[k]: continue
        
        while p[k]:
            cnt += 1
            p[k] -= 1

            for key in keys:
                if p[key] and key+k <= limit:
                    p[key] -= 1
                    break
    return cnt

def first(people, limit):
    # 사람 명단 생성
    p = Counter(people)
    cnt = 0
    keys = sorted(p.keys(), reverse=True)
    
    for person in people:
        # 사람이 없으면 패스
        if not p[person]: continue
        
        # 사람 한 명에게 보트 하나 할당
        cnt += 1
        p[person] -= 1
        
        # 짝꿍이 있으면 그 몸무게 -1
        for k in keys:
            if p[k] and k+person <= limit:
                p[k] -= 1
                break
    return cnt