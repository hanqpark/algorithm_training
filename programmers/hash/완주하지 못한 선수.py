# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


from collections import Counter
def sol(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    