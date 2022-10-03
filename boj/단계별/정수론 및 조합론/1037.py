# 221003
# 프로그래머스 1037번 약수
# 분류: 정수론 및 조합론
# 난이도: 브론즈 1
# https://www.acmicpc.net/problem/1037
# 한줄 평: 12의 약수 1, 2, 3, 4, 6, 12 중 1, 12 뺀 나머지 수를 다 주는 거였음 ^^
import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
if n == 1:
    print(pow(*nums, 2))
else:
    nums.sort()
    print(nums[0]*nums[-1])