# 221002
# 백준 2525번 오븐 시계
# 분류: 조건문
# https://www.acmicpc.net/problem/2525
# 한줄 평: ㅈ밥

h, m = map(int, input().split())
work = int(input())

minute = (m+work)%60
tmp = (m+work)//60
hour = h+tmp if h+tmp < 24 else h+tmp-24
print(hour, minute) 