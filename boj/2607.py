# 220826
# BOJ 2607번 비슷한 단어
# 분류: 구현
# 난이도: 실버 3
# https://www.acmicpc.net/problem/2607

# 처음에는 set으로 시도했으나 DOLL과 같은 단어는 D, O, L로 저장이 되어서 포기함
# 두번째는 Counter로 시도했으나 바꾸는 경우가 해결되지 않아 포기함
# 마지막에는 더하기, 빼기, 바꾸기 경우의 수를 각각 나누어 해결하였음

import sys
from collections import deque
read = sys.stdin.readline

cnt = 0
for i in range(int(read())):
    if not i:
        base = list(read().strip())
    else:
        word = list(read().strip())
        # 빼기를 진행할 경우
        if len(base) > len(word):
            base_tmp = deque(base)
            for _ in base:
                c = base_tmp.popleft()
                try: word.remove(c)
                except: base_tmp.append(c)
            # print(base_tmp, word)
            if len(word)+len(base_tmp)==1:
                cnt += 1
        # 더하기를 진행할 경우
        elif len(base) < len(word):
            word = deque(word)
            base_tmp = base.copy()
            for _ in range(len(word)):
                c = word.popleft()
                try: base_tmp.remove(c)
                except: word.append(c)
            # print(base_tmp, word)
            if len(word)+len(base_tmp)==1:
                cnt += 1
        # 바꾸기를 진행할 경우
        else:
            base_tmp = deque(base)
            for _ in base:
                c = base_tmp.popleft()
                try: word.remove(c)
                except: base_tmp.append(c)
            # print(base_tmp, word)
            if len(word)+len(base_tmp)<3:
                cnt += 1
    # print(cnt)
print(cnt)