from collections import Counter

n = int(input())
sang = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

c = Counter(sang)
res = [c[n] for n in nums]
print(*res)