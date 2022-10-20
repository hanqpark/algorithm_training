# 221009
# 프로그래머스 24416 연산자 끼워넣기
# 분류: 동적 계획법 1
# 난이도: 브론즈 1
# https://www.acmicpc.net/problem/24416
# 한줄 평: 진짜로 재귀 구현하면 터지는 문제

n = int(input())
fib = [0, 1, 1]
for i in range(3, n+1):
    fib.append(fib[i-1]+fib[i-2])
print(fib[-1], 0 if n < 3 else n-2)
