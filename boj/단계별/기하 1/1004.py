# 221003
# 프로그래머스 1004번 어린 왕자
# 분류: 기하 1
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1004
# 한줄 평: 두 점이 같은 원 안에 있을 경우도 고려하여 문제를 풀어야 함

import sys
from math import sqrt
read = sys.stdin.readline

for _ in range(int(read())):
    x1, y1, x2, y2 = map(int, read().split())
    res = 0
    for _ in range(int(read())):
        x, y, r = map(int, read().split())
        if (sqrt((x1-x)**2+(y1-y)**2) < r and sqrt((x2-x)**2+(y2-y)**2) > r) \
            or (sqrt((x1-x)**2+(y1-y)**2) > r and sqrt((x2-x)**2+(y2-y)**2) < r): 
            res += 1
    print(res)