# https://leetcode.com/problems/cheapest-flights-within-k-stops/

import heapq
import collections

def find_cheapest_price(flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v,w))
    
    Q = [(0,src,K)]
    
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price+w
                heapq.heappush(Q, (alt,v,k-1))
    return -1

if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    print(find_cheapest_price(flights, src=0, dst=3, K=1))