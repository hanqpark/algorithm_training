# 반례: 12 = 4+4+4
from itertools import combinations_with_replacement as comb

n = int(input())
nums = list(i*i for i in range(1, int(n**0.5)+1))
if n in nums:
    print(1)
elif n in list(map(sum, comb(nums, 2))):
    print(2)
elif n in list(map(sum, comb(nums, 3))):
    print(3)
else:
    print(4)
