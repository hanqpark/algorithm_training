# 221005
# 프로그래머스 14888 연산자 끼워넣기
# 분류: 백트래킹
# 난이도: 실버 1
# https://www.acmicpc.net/problem/14888
# 한줄 평: https://velog.io/@kimdukbae/BOJ-14888-연산자-끼워넣기-Python -> 백트래킹에 대해 파악할 수 있었다.

import sys
read = sys.stdin.readline

def operate(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return int(a/b)     # a//b 이렇게 했다가 틀림
    

def pypy():
    from itertools import permutations
    
    n = int(read())
    nums = list(map(int, read().split()))
    op, oplist = [], ["+", "-", "*", "/"]
    for o, i in zip(oplist, map(int, read().split())):
        for _ in range(i):
            op.append(o)

    maxi, mini = float("-inf"), float("inf")
    for o in permutations(op):
        res = nums[0]
        for i in range(n-1):
            res = operate(res, nums[i+1], o[i])
        maxi = max(maxi, res)
        mini = min(mini, res)

    print(maxi)
    print(mini)


def dfs(depth, total, pl, mi, mu, di):
    global maxi, mini, n
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    if pl:
        dfs(depth+1, total+nums[depth], pl-1, mi, mu, di)
    if mi:
        dfs(depth+1, total-nums[depth], pl, mi-1, mu, di)
    if mu:
        dfs(depth+1, total*nums[depth], pl, mi, mu-1, di)
    if di:
        dfs(depth+1, int(total/nums[depth]), pl, mi, mu, di-1)

if __name__ == "__main__":
    n = int(read())
    nums = list(map(int, read().split()))
    op = list(map(int, read().split()))
    maxi, mini = float("-inf"), float("inf")
    dfs(1, nums[0], op[0], op[1], op[2], op[3])
    print(maxi)
    print(mini)