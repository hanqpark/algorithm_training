num, res = 1, [0 for _ in range(10)]
for _ in range(3):
    num *= int(input())
for n in str(num):
    res[int(n)] += 1
for r in res:
    print(r)
    