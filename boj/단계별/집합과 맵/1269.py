# 221003
# 프로그래머스 1269번 대칭 차집합
# 분류: 집합과 맵
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1269
# 한줄 평: ㅈ밥

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a-b)+len(b-a))