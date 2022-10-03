# 221003
# 프로그래머스 11051번 이항 계수 2
# 분류: 정수론 및 조합론
# 난이도: 실버 3
# https://www.acmicpc.net/problem/11051
# 한줄 평: https://url.kr/rng2b6 -> 이항 계수가 뭔지 까먹은 -틀-
from math import prod

n, k = map(int, input().split())
print(prod(i+1 for i in range(n)) // prod(i+1 for i in range(k)) // prod(i+1 for i in range(n-k)) % 10007)