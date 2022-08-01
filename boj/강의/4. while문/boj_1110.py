'''더하기 사이클'''

n = int(input())
new = 0
temp = n
cycle = 0
while True:
    cycle += 1
    if temp < 10:
        new = temp*11
    else:
        new = temp%10*10 + (temp//10+temp%10)%10
    if new == n:
        break
    temp = new
print(cycle)
