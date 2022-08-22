'''
푼 날짜: 2022.08.22
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12936
문제 이름: 줄 서는 방법
해결 과정
 1. 처음에는 itertools permutations로 무지성 해결을 하려고 하였으나 개털림
 2. 그 다음에는 팩토리얼과 관련된 규칙이 보여서 그 방향으로 풀 수 있도록 계속 접근하였음
 3. list.pop()의 성능이 안좋을까봐 걱정하였으나 n의 크기가 20이하여서 큰 문제가 없었던 듯 하다.
'''

from math import prod

def solution(n, k):
    nums = [i+1 for i in range(n)] 
    npac = prod(nums)
    res = []
    for i in range(n, 0, -1):
        npac //= i
        idx = k//npac if k%npac else k//npac-1
        res.append(nums.pop(idx))
        k = k%npac if k%npac else npac
    return res
        
    