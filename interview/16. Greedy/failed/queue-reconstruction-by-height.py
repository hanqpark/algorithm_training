# https://leetcode.com/problems/queue-reconstruction-by-height/
# https://kingofbackend.tistory.com/98

# Greedy 문제의 대부분은 우선순위큐(heapq)를 이용하여 푼다고 한다!!!
# 하지만 heapq는 Min 값을 우선으로 뽑기 때문에 lambda를 적절하게 이용하여 정렬하는 것을 잘 활용하자

def solution(people):
    ans = []
    people.sort(key=lambda x: (x[0], -x[1]))
    while people:
        person = people.pop()
        ans.insert(person[1], person)
    return ans