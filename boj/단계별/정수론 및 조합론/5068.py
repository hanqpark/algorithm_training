# 221003
# 프로그래머스 5086번 배수와 약수
# 분류: 정수론 및 조합론
# 난이도: 브론즈 3
# https://www.acmicpc.net/problem/5086
# 한줄 평: ㅈ밥

import sys
read = sys.stdin.readline

while True:
    a, b = map(int, read().split())
    if not a and not b: break
    
    if not a%b: print("multiple")
    elif not b%a: print("factor")
    else: print("neither")