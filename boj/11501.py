# 220824
# BOJ 11501번 주식
# 분류: 그리디
# 난이도: 실버 2
# https://www.acmicpc.net/problem/11501
''' 문제 해결 로직
1. 매일 max를 때리니 시간초과 뜸
2. 당일이 max일때 max를 때리는 방법도 내림차순일때 시간초과 뜸
3. 주가를 오름차순으로 따로 저장하여 pop으로 max값 추출하는 방식이면 [3 4 5 6 7 2 3 4]에서 오류 뜸
4. 위 오류를 해결하기 위해 뽑은 값에 대해 기록을 따로 남겨주었음 -> price_idx: dict
'''
import sys
from collections import deque, defaultdict
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    prices = deque(map(int, read().split()))
    
    price_idx = defaultdict(int)
    for price in prices:
        price_idx[price] += 1
        
    maxlist = sorted(prices)
    res, maxi = 0, maxlist.pop()
    while len(prices)>1:
        day = prices.popleft()
        price_idx[day] -= 1
        profit = maxi-day
        if profit > 0:
            res += profit
        if day == maxi:
            while True:
                maxi = maxlist.pop()
                if price_idx[maxi]: break
    print(res)