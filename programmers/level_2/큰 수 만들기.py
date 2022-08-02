# https://velog.io/@soo5717/프로그래머스-큰-수-만들기-파이썬

from collections import deque

def solution(number, k):
    q = deque(number)
    stack = [q.popleft()]
    while q:
        num = q.popleft()
        while stack and k and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack)[:len(stack)-k]
        