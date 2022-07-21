import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville:
        try:
            one = heapq.heappop(scoville)
            if one >= K: return cnt
            two = heapq.heappop(scoville)
            heapq.heappush(scoville, one+two*2)
            cnt += 1
        except IndexError as e:
            return -1
        