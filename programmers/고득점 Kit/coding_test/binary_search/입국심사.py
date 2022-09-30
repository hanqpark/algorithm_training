# Binary Search
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n    # 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사받는 경우
    while left <= right:
        mid = (left+right)//2
        checked = 0
        for time in times:
            checked += mid//time    # checked: 모든 심사관들이 mid분 동안 심사한 사람의 수
            if checked >= n:        # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상 심사하면 탈출     
                break
        if checked >= n:            # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
            answer = mid
            right = mid-1
        elif checked < n:           # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
            left = mid+1
    return answer

# 단순 구현 -> O(n^2)
def first_try(n, times):
    q = list()
    for time in times:
        schedule = [time*(i+1) for i in range(n)]
        q.extend(schedule)
    return sorted(q)[n-1]

# O(n^2)
def second_try(n, times):
    i = 1
    while n:
        for time in times:
            if not i%time: n-=1
            if not n: return i
        i += 1

# Min Heap 이지만 O(n^2)
import heapq
def third_try(n, times):
    heap = list()
    for i in range(n):
        for time in times:
            heapq.heappush(heap, time*(i+1))
        res = heapq.heappop(heap)
    return res