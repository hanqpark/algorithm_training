# 221005
# 프로그래머스 15652 N과 M (4)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15652
# 한줄 평: itertools 원툴 ㅎ

from itertools import combinations_with_replacement

n, m = map(int, input().split())
for c in combinations_with_replacement([i+1 for i in range(n)], m):
    print(*c)