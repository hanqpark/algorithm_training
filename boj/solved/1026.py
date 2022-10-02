n = int(input())
a = map(int, input().split())
b = map(int, input().split())
res = 0
for x, y in zip(sorted(a), sorted(b, reverse=True)):
    res += x*y
print(res)