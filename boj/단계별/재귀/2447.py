# 221003
# 프로그래머스 2447번 별 찍기 - 10
# 분류: 재귀
# 난이도: 실버 1
# https://www.acmicpc.net/problem/2447
# 한줄 평: https://cotak.tistory.com/38 -> 아예 모르겠어서 그냥 블로그 보고 베껴 왔음... 재귀 구현이 제일 어렵다🥺

import sys
sys.setrecursionlimit(10**6)    # 무한 재귀 loop에 빠지지 않게 하기 위해 설정

def append_star(n):
    if n==1:
        return ["*"]
    
    stars = append_star(n//3)
    l = []
    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+' '*(n//3)+s)
    for s in stars:
        l.append(s*3)
    return l

if __name__ == "__main__":
    n = int(input())
    print('\n'.join(append_star(n)))
        