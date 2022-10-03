# 221003
# 프로그래머스 1358번 하키
# 분류: 기하 1
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1358
# 한줄 평: 기준 설정 잘 해야 함 + 범위 조건이 복잡하므로 실수하지 않도록 주의해야 함

import sys
read = sys.stdin.readline

w, h, x, y, p = map(int, read().split())
r = h//2
cnt = 0
for _ in range(p):
    a, b = map(int, read().split())
    # 왼쪽 반원 or 가운데 사각형 or 오른쪽 반원 내에 속할 경우
    if (a < x and ((x-a)**2+(y+r-b)**2)**0.5 <= r) or \
        (x <= a <= x+w and y <= b <= y+h) or \
            (x < a and ((x+w-a)**2+(y+r-b)**2)**0.5 <= r):
        cnt += 1
print(cnt)