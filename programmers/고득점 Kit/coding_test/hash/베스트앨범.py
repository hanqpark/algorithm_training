# 220921
# 프로그래머스 42579번 겹치는 건 싫어
# 분류: 해시
# 난이도: 레벨 3
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# 참고 : https://weejw.tistory.com/374 -> list 안에서 동일한 값의 index를 여러 개 뽑아오는 코드
# 변수 명을 너무 더럽게 썼다... 이런 부분도 주의해서 풀 것.

from collections import defaultdict

def solution(genres, plays):
    # 가장 많이 들은 장르를 계산하는 코드
    best = defaultdict(list)
    for g, p in zip(genres, plays):
        best[g].append(p)
    hits = sorted(set(genres), key=lambda x: sum(best[x]), reverse=True)
    
    best_album = list()
    # 수록 기준 1
    for h in hits:
        # 수록 기준 2
        count = sorted(best[h], reverse=True)
        for i in range(min(len(count), 2)):
            # 수록 기준 3
            # list 안에서 동일한 값의 index를 여러 개 뽑아오는 코드
            tmp = list(filter(lambda x: plays[x]==count[i], range(len(plays))))
            for t in tmp:
                if t not in best_album:
                    best_album.append(t)
                    break
            
    return best_album
    