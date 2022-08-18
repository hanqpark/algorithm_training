# 2022.08.18
# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

''' 참고한 사이트
https://www.acmicpc.net/board/view/81295    예외 테스트케이스 확인하였음
https://hongcoding.tistory.com/92           idx dictionary 풀이 로직 참고하였음 '''

import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

for _ in range(int(read())):
    heap = []                               # 최소 힙 생성
    maxheap = []                            # 최대 힙 생성
    idx = defaultdict(int)                  # pop 작업을 할 때 최소 힙 or 최대 힙 중 한 곳에서만 나오기 때문에 값이 사라졌다는 것을 표시할 dictionary
    for _ in range(int(read())):
        exe, num = read().split()
        num = int(num)
        if exe == "I":
            heapq.heappush(heap, num)       # 최소 힙에 값 넣어주기
            heapq.heappush(maxheap, -num)   # 최대 힙에 값 넣어주기
            idx[num]+=1                     # 처음엔 bool로 해줬는데 값이 중복으로 입력되는 경우가 있어서 int로 바꿈
        else:
            if num == 1:
                while maxheap:
                    maxi = heapq.heappop(maxheap)   # 최대 힙에서 값 빼주고
                    if idx[-maxi]:                  # 이미 최소 힙에서 뺀 값이면 while문 돌게 설정
                        idx[-maxi]-=1               # 최대 힙에서 값을 뺐다는 것을 idx에 기록
                        break
            else:
                while heap:
                    mini = heapq.heappop(heap)      # 최소 힙에서 값 빼주고
                    if idx[mini]:                   # 이미 최대 힙에서 뺀 값이면 while문 돌게 설정
                        idx[mini]-=1                # 최소 힙에서 값을 뺐다는 것을 idx에 기록
                        break
    res = [k for k, v in idx.items() if v]
    if res: print(max(res), min(res))
    else: print("EMPTY")