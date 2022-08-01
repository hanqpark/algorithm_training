# https://leetcode.com/problems/task-scheduler/

# collections Counter 를 아주 기가 막히게 사용하였음
#   1. Counter.most_common
#   2. Counter.subtract
#   3. counter += Counter()

from collections import Counter

def sol(tasks, n):
    counter = Counter(tasks)
    res = 0
    
    while True:
        cnt = 0
        for task, _ in counter.most_common(n+1):
            cnt += 1
            res += 1
            counter.subtract(task)
            counter += Counter()    # 0 이하인 아이템을 목록에서 제거
        if not counter: break
        res += n-cnt+1
    return res