# 220829
# BOJ 5430번 AC
# 난이도: 골드 5
# https://www.acmicpc.net/problem/5430

'''문제 풀이 핵심
1. list를 str로 받아와서 str로 출력해야 한다...
2. R이 reverse라고 진짜 reverse 때리면 시간초과 뜬다.
3. input 받을 때 [, ], \n 이런 쓰잘데기 없는 것들 잘 처리해주는 것이 중요하다.
4. sorted(), reversed() 헷갈리지 말 것.
5. 쉬운 문제이지만 각종 제약 조건이 도처에 깔려 있어 이런 것들을 제거해주면 시간이 꽤 걸리는 문제... 실제 코테에서 이런 문제를 만나지 않기를 바라본다. '''

import sys
from collections import deque
read = sys.stdin.readline

for _ in range(int(read())):
    p = read().strip()
    n = int(read())
    ''' 배열을 받아오는 작업 -> 여기서 오래 걸림
    strip할 문자들은 " " 안에 때려 박으면 됨
    굳이 int로 바꿔준 이유는 빈 배열을 그냥 deque으로 저장해주면 '\n'이 저장됨
    \n은 int로 바뀔 때 오류가 뜨니 -> except에서 빈 덱으로 바꿔줌 '''
    try:
        lst = deque(map(int, read().strip("[]\n").split(",")))
    except:
        lst = deque()
    ''' 함수를 실행하는 작업 
    R: 실제로 배열을 뒤집는 것이 아니라 앞에서 뺄지 뒤에서 뺄지 결정
    D: R에서 정해진 값에 따라 빼줌. 빈 배열이면 error 때리고 break '''
    rev = False
    for c in p:
        if c == "R":
            rev = False if rev else True
        elif c == "D":
            try:
                _ = lst.pop() if rev else lst.popleft()
            except:
                lst = "error"
                break
    ''' 결과 값을 출력하는 작업
    list 출력이 아니라 string 출력임 '''
    if type(lst) == deque:
        lst = list(reversed(lst)) if rev else list(lst)
        print("["+",".join(map(str,lst))+"]")
    else:
        print(lst)