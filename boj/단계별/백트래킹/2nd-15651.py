# 221020
# 프로그래머스 15651 N과 M (3)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15651
# 한줄 평: 백트의 기초는 익혔다

def dfs(depth, start):
    if depth == m:
        print(*arr)
    else:
        for i in range(start, n):
            arr[depth] = i+1
            dfs(depth+1, start)

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [0]*m
    dfs(0, 0)