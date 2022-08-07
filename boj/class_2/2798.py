from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = [sum(i) for i in list(combinations(cards, 3)) if sum(i) <= m]
print(max(res))