# 2022.08.19
# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 예상 대진표

# 12...1516, 1234....13141516, 12345678 / 910111213141516, 12345678910111213141516 이런 식으로 풀을 늘려나가는 방식으로 풀었음
def solution(n,a,b):
    round, cnt = 2, 1       # 12, 1234의 길이에 해당하는 것이 round, 길이가 늘어날 때마다 cnt를 하나씩 늘려줌                  
    while round <= n:       
        for i in range(n//round):   # n//round는 n강이라고 보면 됨
            tmp = [i*round+(x+1) for x in range(round)]     # n이 8일때 [1,2] [3,4] [5,6] [7,8] 이런식으로 모든 경기를 훑어준다고 보면 됨 (완전 탐색) 
            if a in tmp and b in tmp:
                return cnt
        round *= 2
        cnt += 1