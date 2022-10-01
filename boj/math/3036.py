
# 성공
from math import gcd
n = int(input())
for i, num in enumerate(map(int, input().split())):
    if not i: first=num
    else: 
        g = gcd(first, num)
        res = f"{first//g}/{num//g}"
        print(res)


# 출력 초과 -> 실패: Fraction 굳이 사용할 필요 없을 듯
from fractions import Fraction
n = int(input())
for i, num in enumerate(map(int, input().split())):
    if not i: first=num
    else: 
        fr = str(Fraction(first/num))
        res = fr if '/' in fr else f"{fr}/1"
        print(res)