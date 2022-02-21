import sys
read = sys.stdin.readline
info = []
n = int(read())
for i in range(n):
    x, y = map(int, read().split())
    info.append([x, y, i+1, 1]) # 몸무게, 키, 번호, 순위
weight = sorted(info, reverse=True)


for i in range(1, n):
    temp = i
    while weight[temp][1] > weight[temp-1][1]:
        temp -= 1
    weight[i][-1] = temp+1
ans = sorted(weight, key=lambda x: x[-2])
print(" ".join([str(a[-1]) for a in ans]))