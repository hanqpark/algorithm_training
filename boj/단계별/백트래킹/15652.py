# 221005
# 프로그래머스 15652 N과 M (4)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15652
# 한줄 평: itertools 원툴 ㅎ / backtracking 정복

from itertools import combinations_with_replacement
def first_try():
    n, m = map(int, input().split())
    for c in combinations_with_replacement([i+1 for i in range(n)], m):
        print(*c)
        
        
def dfs(depth, start):
    if depth == m:
        print(*arr)
    else:
        for i in range(1, n+1):
            if not arr or arr[-1] <= i:
                arr.append(i)
                dfs(depth+1, start)
                arr.pop()
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    dfs(0, 1)