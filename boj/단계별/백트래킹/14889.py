# 221005
# 프로그래머스 14889 스타트와 링크
# 분류: 백트래킹
# 난이도: 실버 2
# https://www.acmicpc.net/problem/14889
# 한줄 평: 원래 삼성 코테에서는 itertools, sys를 사용 못해서 백트래킹으로 푸는 것이 정석이라고 한다.

import sys
from collections import deque
from itertools import combinations
read = sys.stdin.readline

# 조건 받아오기
n = int(read())
link = [list(map(int, read().split())) for _ in range(n)]

# 문풀 변수 설정
mini = float("inf")
nums = [i for i in range(n)]
combs = list(combinations(nums, n//2))

# 가능한 모든 팀 조합으로 계산
for i, p in enumerate(combs):
    if i == len(combs): break       # 1,2,3 ~ 4,5,6 두 번씩 계산되므로 절반만 수행하도록
    
    # 우리 팀 시너지 점수 구하기
    me = deque(p)
    my_score = 0
    for _ in range(len(me)):
        tmp = me.popleft()
        for m in me:
            my_score += link[tmp][m]
        me.append(tmp)
    
    # 상대 팀 시너지 점수 구하기
    you = deque(set(nums)-set(p))
    your_score = 0
    for _ in range(len(you)):
        tmp = you.popleft()
        for y in you:
            your_score += link[tmp][y]
        you.append(tmp)
    
    # 최소 시너지 점수 구하기
    mini = min(mini, abs(my_score-your_score))
print(mini)