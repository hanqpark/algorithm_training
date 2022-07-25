# 해설 영상: https://www.youtube.com/watch?v=z4wKvYdd6wM
from itertools import permutations

# https://ko.wikipedia.org/wiki/여덟_퀸_문제
def just_kidding(n):
    ans = [0,1,0,0,2,10,4,40,92,352,724,2680,14200]
    return ans[n]

# 순열을 이용하여 해결한 풀이
def permutation(n):
    cols = range(n)
    result = 0
    for vec in permutations(cols):
        a = set(vec[i]+i for i in cols)
        b = set(vec[i]-i for i in cols)
        if n == len(a) == len(b):
            result+=1
    return result

# DFS를 이용하여 해결한 풀이
def check(lst, col, row) :
    for c in range(col) :
        if lst[c] == row : return False # 같은 row
        if (col-c) == abs(row-lst[c]) : return False # 같은 대각선
    return True

def dfs(lst, col, n) :
    result = 0
    for idx in range(n) :
        if check(lst, col, idx):
            lst[col] = idx
            if col == n-1 : result += 1
            else : result += dfs(lst, col+1, n)
    return result

def solution(n):
    return dfs([0]*n, 0, n)


if __name__ == "__main__":
    res = solution(4)
    print(res)