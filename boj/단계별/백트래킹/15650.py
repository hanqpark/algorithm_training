# 221005
# 프로그래머스 15650 N과 M (2)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15650
# 한줄 평: w밥 -> 백트래킹 연습 안해서 줘털렸다... + 백트래킹 푸는 방법에 여러가지가 있더라

def first():
    import sys
    from itertools import combinations
    read = sys.stdin.readline

    n, m = map(int, read().split())
    for c in combinations([i+1 for i in range(n)], m):
        print(*c)
        

# answer에 미리 임의의 값을 채워넣고 수정하는 방식으로 백트래킹 진행         
def solve(depth, start):
    if depth == n:
        print(*arr)
        return
    for i in range(start, m):
        arr[depth] = i+1
        solve(depth+1, i+1)

# answer에 append, pop 해주는 방식으로 백트래킹 진행
def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
    else:
        for i in range(n):
            if not answer or answer[-1] < i+1:
                answer.append(i+1)
                dfs(depth+1, n, m)
                answer.pop()
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    answer = []
    arr = [0 for _ in range(n)]
    dfs(0, n, m)
    solve(0, 0)
