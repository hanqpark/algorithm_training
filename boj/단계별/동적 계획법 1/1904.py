# 221009
# 프로그래머스 1904 01타일
# 분류: 동적 계획법 1
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1904
# 한줄 평: n=1, 2 일 때 주의해주도록 하자

res = [0, 1, 2]
n = int(input())
for i in range(3, n+1):
    res.append((res[i-1]+res[i-2])%15746)
print(res[-1] if n > 2 else res[n])