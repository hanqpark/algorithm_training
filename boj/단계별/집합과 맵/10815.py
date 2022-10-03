# 221003
# 프로그래머스 10815번 숫자 카드
# 분류: 집합과 맵
# 난이도: 실버 5
# https://www.acmicpc.net/problem/10815
# 한줄 평: ㅈ밥

import sys
from collections import defaultdict
read = sys.stdin.readline

n = int(read())
sang = defaultdict(int)
for i in map(int, read().split()):
    sang[i] = 1

m = int(read())
res = []
for me in map(int, read().split()):
    tmp = 1 if sang[me] else 0
    res.append(tmp)
print(*res)