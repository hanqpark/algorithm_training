# 221003
# 프로그래머스 2981번 검문
# 분류: 정수론 및 조합론
# 난이도: 골드 4
# https://www.acmicpc.net/problem/2981
# 한줄 평: https://tmdrl5779.tistory.com/94 -> 내 머리로는 도저히 생각해낼 수 없었던 문제였다.
import sys
from math import gcd
read = sys.stdin.readline

nums = sorted(int(read()) for _ in range(int(read())))
interval = []
for i in range(1, len(nums)):               # A-B = M(a-b)
    interval.append(nums[i]-nums[i-1])      # B-C = M(b-c) -> M이 최대공약수

M = interval[0]
for i in range(1, len(interval)):
    M = gcd(M, interval[i])           # A-B, B-C, ..., 의 최대공약수 M 구하기

ans = []
for i in range(2, int(M**0.5)+1):     # 공약수의 몫, 나머지를 함께 구해 제곱근으로 범위 좁히기
    if not M%i:
        ans.append(i)
        ans.append(M//i)
ans.append(M)                         # 자기 자신도 추가
print(*sorted(set(ans)))