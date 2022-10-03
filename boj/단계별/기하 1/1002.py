# 221003
# 프로그래머스 1002번 터렛
# 분류: 기하 1
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1002
# 한줄 평: https://ooyoung.tistory.com/111 -> 학창시절에 배운 두 원의 점점 개수 구하기 구현 문제... 다 까먹었지 ㅎ;
import sys
from math import sqrt
read = sys.stdin.readline
for _ in range(int(read())):
    x1, y1, r1, x2, y2, r2 = map(int, read().split())
    c2c = sqrt((x1-x2)**2+(y1-y2)**2)
    if c2c==0 and r1==r2:                   # 동심원 + 반지름 동일
            print(-1)
    elif c2c == r1+r2 or c2c == abs(r1-r2): # 내접 + 외접
        print(1)
    elif abs(r1-r2) < c2c < r1+r2:          # 두 점에서 만날 때 (안, 밖)
        print(2)
    else:                                   # 그 외 만나지 않는 모든 경우
        print(0)