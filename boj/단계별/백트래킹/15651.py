# 221005
# 프로그래머스 15651 N과 M (3)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15651
# 한줄 평: 개털렸음.. 똑같이 재귀로 구현했으나 나는 공간복잡도가 초과해서 망했다
        # https://jiwon-coding.tistory.com/23
from copy import deepcopy
def first_try(lst, m):
    if not m:
        return lst
    new = []
    for i in range(len(lst)):
        for j in range(1, n+1):
            l = deepcopy(lst[i])
            l.append(j)
            new.append(l)
    return first_try(new, m-1)
''' Fisrt Try
n, m = map(int, input().split())
lst = list([i+1] for i in range(n))
for w in second_try(lst, m-1):
    print(*w)
'''

def recur(stack):
    if len(stack) == m:
        print(*stack)
        return
    for i in range(1, n+1):
        stack.append(i)
        recur(stack)
        stack.pop()
n, m = map(int, input().split())
stack = []
recur(stack)
    