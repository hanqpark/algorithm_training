'''숫자의 개수'''

a = int(input())
b = int(input())
c = int(input())
res = str(a*b*c)
cnt = [0 for _ in range(10)]
for r in res:
    cnt[int(r)] += 1
for c in cnt:
    print(c)