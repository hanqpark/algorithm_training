# 220827
# BOJ 11659번 구간 합 구하기 4
# 난이도: 실버 3
# https://www.acmicpc.net/problem/11659

# 문제 풀이 핵심
# 1. : 로 리스트 나누는 것은 오래 걸린다
# 2. 구간 합을 구하는 것이니 구간 -> DP로 접근하는 것이 옳은듯

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
nums = list(map(int, read().split()))
# 구간 합 미리 구해 놓기 -> O(n)
sums = [0]
for x in range(len(nums)):
    sums.append(sums[x]+nums[x])
# 미리 구해놓은 구간 합에 접근하는 시간 -> O(1)
for _ in range(m):
    i, j = map(int, read().split())
    print(sums[j]-sums[i-1])