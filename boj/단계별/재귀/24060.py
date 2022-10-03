# 221003
# 프로그래머스 24060번 알고리즘 수업 - 병합 정렬 1
# 분류: 재귀
# 난이도: 실버 4
# https://www.acmicpc.net/problem/24060
# 한줄 평: 병합 정렬은 middle을 어디서 나누느냐에 따라 중간 과정이 많이 바뀜...주의해야 할 듯
from math import ceil
from collections import deque

def merge(front, back):
    global cnt, answer
    front, back = deque(front), deque(back)
    res = []
    while front or back:
        if front and back:
            if front[0] <= back[0]:
                res.append(front.popleft())
            else:
                res.append(back.popleft())
        elif front:
            res.append(front.popleft())
        elif back:
            res.append(back.popleft())
        if cnt < k:             # cnt가 k일때까지만 집계해주기
            cnt += 1
            answer = res[-1]
        # print(cnt, answer)
    return res        

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = ceil(len(l) / 2)      # list가 홀수면 front가 더 많도록 middle을 설정 
    left = l[:mid]
    right = l[mid:]
    front = merge_sort(left)
    back = merge_sort(right)
    return merge(front, back)

if __name__ == "__main__":
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    cnt, answer = 0, 0
    result = merge_sort(l)
    a = -1 if cnt != k else answer      # cnt가 k가 안됐으면 조건에 부합하지 않으니 -1
    print(a)