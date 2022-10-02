# 221002
# 백준 3003번 네트워크
# 분류: 입출력 구현
# https://www.acmicpc.net/problem/3003
# 한줄 평: ㅈ밥

basic, answer = [1, 1, 2, 2, 2, 8], []
for b, p in zip(basic, map(int, input().split())):
    answer.append(b-p)
print(*answer)