import sys, heapq
from collections import defaultdict
read = sys.stdin.readline

cnt = defaultdict(int)
heap = []

for _ in range(int(read())):
    n = int(read())
    if n == 0:
        res = 0 if not heap else heapq.heappop(heap)
        if cnt[-res]:
            cnt[-res] -= 1
            print(-res)
        else:
            cnt[res] -= 1
            print(res)
    else:
        cnt[n] += 1
        heapq.heappush(heap, abs(n))