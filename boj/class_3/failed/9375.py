# 2022.08.17
# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈
# 실패

import sys
from math import prod
from collections import defaultdict
from itertools import combinations
read = sys.stdin.readline


def first():
    for _ in range(int(read())):
        clothes = defaultdict(int)
        for _ in range(int(read())):
            name, kind = read().split()
            clothes[kind] += 1              # 옷의 종류 개수만 카운트해준다
        res = 0
        for i in range(1, len(clothes)+1):
            res += sum(map(prod, combinations(clothes.values(), i)))    # 종류가 3개라면 하나 입었을때, 두 종류 입었을 때, 세 종류 입었을 때를 조합으로 계산하여 곱을 구한 다음 값을 다 더하는 방향으로 진행함
        print(res)                                                      # 그랬더니 시간 초과가 발생함.. 아마 조합의 수가 프로그래머스 문제와 달리 4개 이상인듯

for _ in range(int(read())):
    clothes = defaultdict(int)
    for _ in range(int(read())):
        name, kind = read().split()
        clothes[kind] += 1
    res = 1
    for v in clothes.values():
        res *= v+1              # +1은 아무것도 입지 않았을 경우
    print(res-1)                # -1은 발가벗고 있는 경우의 수
    
