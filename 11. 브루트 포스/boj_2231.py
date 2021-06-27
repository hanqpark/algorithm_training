n = int(input())
op = []
for i in range(n+1):
    temp, sum = i, i
    while temp:
        sum += temp%10
        temp //= 10
    if sum == n: op.append(i)
print(min(op) if op else 0)