# 221003
# 프로그래머스 14425번 문자열 집합
# 분류: 집합과 맵
# 난이도: 실버 3
# https://www.acmicpc.net/problem/14425
# 한줄 평: ㅈ밥
import sys
from collections import defaultdict
read = sys.stdin.readline

n, m = map(int, read().split())
s = defaultdict(int)
for _ in range(n):
    s[read().strip()] = 1

cnt = 0
for _ in range(m):
    if s[read().strip()]: cnt += 1
print(cnt)
