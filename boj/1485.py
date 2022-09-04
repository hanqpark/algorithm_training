# 220902
# BOJ 17626번 정사각형
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1485

# 문제 풀이 핵심
# 마름모로 생긴 정사각형도 존재한다...

import sys
from math import sqrt
read = sys.stdin.readline

for _ in range(int(read())):
    res = 0
    points = []
    for _ in range(4):
        points.append(list(map(int, read().split())))
    # 변 길이, 대각선 길이 외 다른 길이가 추가되면 0을 return
    leng = set()
    for i in range(4):
        x, y = points[i]
        for j in range(i+1, 4):
            a, b = points[j]
            leng.add(sqrt(pow(x-a, 2)+pow(y-b, 2)))
    res = 1 if len(leng)==2 else 0
    print(res)
    