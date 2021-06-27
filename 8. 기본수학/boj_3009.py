xs, ys = [], []
x1, y1 = '', ''
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

for i in range(3):
    if xs.count(xs[i]) == 1: x1 = xs[i]
    if ys.count(ys[i]) == 1: y1 = ys[i]
print(x1, y1)