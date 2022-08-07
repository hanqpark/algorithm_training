n = int(input())
time = sorted(list(map(int, input().split())))
res = [sum(time[:i+1]) for i in range(n)]
print(sum(res))