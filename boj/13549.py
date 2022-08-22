from collections import deque, defaultdict

def main(n, k):
    visited = defaultdict(int)
    dq = deque([[n, 0]])
    while dq:
        now, cnt = dq.popleft()
        if now<0 or now>100000 or visited[now] and visited[now]<cnt:
            continue
        visited[now] = cnt
        dq.append([now*2, cnt])
        dq.append([now+1, cnt+1])
        dq.append([now-1, cnt+1])
    return visited


if __name__ == "__main__":
    n, k = map(int, input().split())
    res = main(n, k)
    print(res)