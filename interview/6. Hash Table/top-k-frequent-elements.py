# https://leetcode.com/problems/top-k-frequent-elements

import heapq
import collections
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

def heap(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    
    return topk

heap([1,2], 2)