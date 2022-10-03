# 221003
# 프로그래머스 1021번 회전하는 큐 
# 분류: 큐, 덱
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1021
# 한줄 평: deque의 rotate 함수 방향을 헷갈리지 맙시다!

from collections import deque

n, m = map(int, input().split())
poplist = map(int, input().split())
nums = deque(i+1 for i in range(n))

cnt = 0
for num in poplist:
    idx = nums.index(num)
    if idx:
        if idx <= len(nums)-idx:
            nums.rotate(-idx)
            cnt += idx
        else:
            nums.rotate(len(nums)-idx)
            cnt += len(nums)-idx
    nums.popleft()
print(cnt)
        