import sys
from collections import Counter
read = sys.stdin.readline

n = int(read())
nums = [int(read()) for _ in range(n)]

if n == 1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)
else:
    print(round(sum(nums)/n))

    print(sorted(nums)[n//2])

    c = [[k, v] for k, v in Counter(nums).items()]
    c.sort(key=lambda x: (-x[1], x[0]))
    res = c[0][0] if c[0][1] != c[1][1] else c[1][0]
    print(res)

    print(max(nums)-min(nums))