n = int(input())
minval = 0
if not n%3: minval = n//3
cnt = 0
while n%5 and n>0:
    cnt += 1
    n -= 3
if n < 0:
    print(-1)
else:
    cnt += n//5
    print(min(cnt, minval) if minval else cnt)