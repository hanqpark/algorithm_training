from collections import deque

def solution(n, words):
    words = deque(words)
    used = []
    end = None
    res = [1,1] # 사람, 차례
    while words:
        word = words.popleft()
        
        # 사용했던 단어일 경우 탈락
        if word in used:
            return res
        
        # 안이어지는 단어일 경우 탈락
        if end and end != word[0]:
            return res
        
        # result update
        if res[0] == n:
            res[0] = 1
            res[1] += 1
        else:
            res[0] += 1
        end = word[-1]
        used.append(word)
    return [0,0]
        