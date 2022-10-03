# 221003
# 프로그래머스 11478번 서로 다른 부분 문자열의 개수
# 분류: 집합과 맵
# 난이도: 실버 3
# https://www.acmicpc.net/problem/11478
# 한줄 평: 

s = input()
res = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        res.add(s[i:j])
print(len(res))