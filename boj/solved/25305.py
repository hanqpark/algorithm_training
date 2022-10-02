# 221002
# 백준 25305번 커트라인
# 분류: 정렬
# 난이도: 브론즈 2
# https://www.acmicpc.net/problem/25305
# 한줄 평: ㅈ밥

n, k = map(int, input().split())
print(sorted(list(map(int, input().split())), reverse=True)[k-1])