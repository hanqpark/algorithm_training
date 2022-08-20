def dp(n):
    res = [0, 1, 2]
    for i in range(3, n+1):
        res.append((res[i-1]+res[i-2])%1234567)
    return res[n]


# 실패 + 시간초과
from collections import deque
def bfs(n):
    dq = deque([0])
    cnt = 0
    while dq:
        now = dq.popleft()
        if now == n:
            cnt += 1
        elif now < n:
            dq.append(now+1)
            dq.append(now+2)
    return cnt


# 시간초과 + 런타임에러
def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n < 1:
        return 0
    else:
        return recursion(n-1)+recursion(n-2)
