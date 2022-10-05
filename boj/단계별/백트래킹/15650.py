# 221005
# 프로그래머스 15650 N과 M (2)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15650
# 한줄 평: w밥

import sys
from itertools import combinations
read = sys.stdin.readline

n, m = map(int, read().split())
for c in combinations([i+1 for i in range(n)], m):
    print(*c)