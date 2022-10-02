# 221002
# 백준 2480번 주사위 세개
# 분류: 조건문
# https://www.acmicpc.net/problem/2480
# 한줄 평: ㅈ밥인데 15번째 줄 same[1]을 dices[same[1]]로 적어서 틀렸음...

from collections import Counter

dices = Counter(map(int, input().split()))
same = list(dices.keys())
award = 0
if len(same) == 1:
    award = 10000+same[0]*1000
elif len(same) == 2:
    s = same[0] if dices[same[0]]==2 else same[1]
    award = 1000+s*100
elif len(same) == 3:
    award = max(same)*100
print(award)