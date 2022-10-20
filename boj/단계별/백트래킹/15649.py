# 221020
# 프로그래머스 15649 N과 M (1)
# 분류: 백트래킹
# 난이도: 실버 3
# https://www.acmicpc.net/problem/15651
# 한줄 평: 백트래킹의 기초... 2022 하반기 코테에 자주 출몰했으므로 기초부터 다져놓자

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
    else:
        for i in range(1, n+1):
            if not visited[i-1]:
                answer.append(i)
                visited[i-1] = True
                dfs(depth+1, n, m)
                answer.pop()
                visited[i-1] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False for _ in range(n)]
    answer = []
    dfs(0, n, m)