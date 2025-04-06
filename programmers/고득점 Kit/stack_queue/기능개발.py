# 1st solution -> spd.popleft() 안해줘서 통과 안됨 ㄹㅇㅋㅋ
from collections import deque
def solution(progresses, speeds):
    prog, spd, res, cnt = deque(progresses), deque(speeds), [], 0
    while prog:
        for i in range(len(prog)): prog[i] += spd[i]
        for p in prog:
            if p < 100: break
            else: cnt += 1
        if cnt:
            res.append(cnt)
            for _ in range(cnt): prog.popleft(); spd.popleft()
            cnt = 0
    return res
        
            

# 2nd solution -> 완전 오답
def sol2(progresses, speeds):
    prog_left = [100-p for p in progresses]
    days_left = [p//s+1 for p, s in zip(prog_left, speeds)]
    res, cnt = [], 1
    for i in range(1, len(days_left)):
        if days_left[i-1] < days_left[i]:
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
    res.append(cnt)
    return res


if __name__ == "__main__":
    progresses = list(map(lambda x: int(x), input().split()))
    speeds = list(map(lambda x: int(x), input().split()))
    print(progresses, speeds)
    res = solution(progresses, speeds)
    print(res)