# 2022.08.23 화요일
# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# n^2 배열 자르기

# 처음에는 무지성 for loop 2개 돌려서 풀었지만 n의 크기가 너무 커서 실패..
# n 사이즈를 최대한 줄여서 for loop 2개 돌리자는 마인드로 접근하여 성공
# 하지만 많이 느린 편

def solution(n, left, right):
    ans = []
    for i in range(left//n, right//n+1):
        for j in range(n):
            if i==left//n and j<left%n:
                continue
            if i==right//n and j>right%n:
                break
            ans.append(max(i+1, j+1))
    return ans