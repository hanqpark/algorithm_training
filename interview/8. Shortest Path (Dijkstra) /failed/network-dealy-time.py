# https://leetcode.com/problems/network-delay-time/

import heapq
import collections

def network_delay_time(times, n, k):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v,w))
    
    Q = [(0,k)]
    dist = collections.defaultdict(int)
    
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time+w
                heapq.heappush(Q, (alt,v))
    
    if len(dist)==n:
        return max(dist.values())
    
    return -1

if __name__ == "__main__":
    times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    print(network_delay_time(times, n, k))