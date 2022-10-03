# 221003
# 프로그래머스 2477번 참외밭
# 분류: 기하 1
# 난이도: 실버 3
# https://www.acmicpc.net/problem/2477
# 한줄 평: https://itcrowd2016.tistory.com/84 -> 패턴을 찾는 것이 어렵다.. 블로그 보고 패턴만 참고함
import sys
from collections import defaultdict
read = sys.stdin.readline

# 참외 지도 생성
cnt = int(read())
k_melon = defaultdict(list)     # 가로, 세로를 파악하기 위함
side = list()                   # 변 그리는 순서를 파악하기 위함
for _ in range(6):
    k, m = map(int, read().split())
    k_melon[k].append(m)
    side.append(m)

# 가로 최대, 세로 최소 구하기
garo_max = max(k_melon[1]+k_melon[2])
garo_max_idx = side.index(garo_max)
try:
    sero_min = abs(side[garo_max_idx+1]-side[garo_max_idx-1])   # idx가 list 마지막이면 +1 했을 때 IndexError 발생
except IndexError:
    sero_min = abs(side[0]-side[garo_max_idx-1])                # 어차피 +1이니 IndexError 발생하면 idx 0으로 고정해주면 됨

# 세로 최대, 가로 최소 구하기
sero_max = max(k_melon[3]+k_melon[4])
sero_max_idx = side.index(sero_max)
try:
    garo_min = abs(side[sero_max_idx+1]-side[sero_max_idx-1])
except IndexError:
    garo_min = abs(side[0]-side[sero_max_idx-1])

# 정답 출력
print((garo_max*sero_max-garo_min*sero_min)*cnt)