# https://leetcode.com/problems/sliding-window-maximum

import time
from collections import deque

def try_1(nums, k):
    res = []
    for i in range(len(nums)-k+1):
        res.append(max(nums[i:i+k]))
    return res

def try_2(nums, k):
    window, nums, ans = deque(), deque(nums), list()
    for _ in range(k-1):
        window.append(nums.popleft())
    while nums:
        window.append(nums.popleft())
        ans.append(max(window))
        window.popleft()
    return ans

def sol(nums, k):
    MIN = float('-inf')
    res, window, maxi = [], deque(), MIN
    
    for i, v in enumerate(nums):
        window.append(v)
        if i < k-1: continue
        
        if maxi==MIN: maxi = max(window)
        elif v > maxi: maxi = v
        res.append(maxi)
        
        if maxi == window.popleft():
            maxi = MIN
    return res

def real_sol(nums, k):
    dq, arr = deque(), list()
    for i, n in enumerate(nums):
        # k개의 윈도우만 유지 되도록 한다. i가 증가될 때 deque의 0번에 있는 인덱스와 같으면 삭제한다. 
        # i - q[0] == k 가 좀 헷갈릴 수 있는데, i, q[0], k 가 각각 3, 0, 3 이라면 아래와 같은 뜻이다.
        # i가 3이면 4번째 인덱스이고 q[0]은 0번째 인덱스이니 유효한 인덱스는 1,2,3 이므로 0번을 삭제하라는 뜻이다. 
        if dq and i - dq[0] == k: 
            dq.popleft()
		
        # nums[i]의 값보다 작은 값들은 모두 삭제한다. 
        # 이 과정을 반복함으로써 max값의 후보의 인덱스만 데크에 남게된다. 
        while dq and n > nums[dq[-1]]: 
            dq.pop()
            
        dq.append(i)
		
        # k 번째부터 결과 리스트에 최대값을 넣는다. 
        if i >= k - 1: 
            arr.append(nums[dq[0]])
    return arr


nums = [i for i in range(10, -10, -1)]
start = time.time()  # 시작 시간 저장
res = real_sol(nums, 3)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간