# 221002
# 백준 25501번 재귀의 귀재
# 분류: 재귀
# 난이도: 브론즈 2
# https://www.acmicpc.net/problem/25501
# 한줄 평: ㅈ밥

def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for _ in range(int(input())):
    print(*is_palindrome(input()))
    