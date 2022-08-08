import sys, heapq
read = sys.stdin.readline

heap = []
for _ in range(int(read())):
    x = int(read())
    if x:
        heapq.heappush(heap, -x)
    else:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)
            