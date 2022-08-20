from collections import deque, defaultdict

n, k = map(int, input().split())
visited = defaultdict(int)
q = deque([[n, 0]])
res, minval = 0, False
while q:
    now, cnt = q.popleft()
    if now == k:
        if minval and cnt == minval:
            res += 1
        elif not minval:
            minval = cnt
            res += 1
    if now<0 or now>100000 or visited[now]>30일 or minval and cnt>=minval:
        continue
    visited[now] += 1
    q.append([now+1, cnt+1])
    q.append([now-1, cnt+1])
    q.append([now*2, cnt+1])
print(minval)
print(res)