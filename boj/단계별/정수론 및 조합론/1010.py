# 221003
# 프로그래머스 1010번 다리 놓기
# 분류: 정수론 및 조합론
# 난이도: 실버 5
# https://www.acmicpc.net/problem/1010
# 한줄 평: ㅈ밥
import sys
from math import prod
read = sys.stdin.readline

for _ in range(int(read())):
    n, m = map(int, read().split())
    print(prod(m-i for i in range(n))//prod(i+1 for i in range(n)))