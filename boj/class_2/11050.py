from itertools import combinations
n, k = map(int, input().split())
nums = [i+1 for i in range(n)]
com = list(combinations(nums, k))
print(len(com))
