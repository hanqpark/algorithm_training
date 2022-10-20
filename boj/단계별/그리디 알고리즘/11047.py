# 221009
# 프로그래머스 11047 동전 0
# 분류: 그리디 알고리즘
# 난이도: 실버 4
# https://www.acmicpc.net/problem/11047
# 한줄 평: 
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coins = [int(read()) for _ in range(n)]
cnt = 0
while k:
    for i in range(len(coins)-1, 0, -1):
        if coins[i] <= k:
            k -= coins[i]
            cnt += 1
            break
print(cnt)