cnt, sum = 0, 0
x = int(input())
while sum < x:
    cnt += 1
    sum += cnt
oneside = sum-x+1
otherside = cnt-sum+x
print(f"{oneside}/{otherside}" if cnt%2==1 else f"{otherside}/{oneside}")
