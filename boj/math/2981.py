nums = [int(input()) for _ in range(int(input()))]
res = []
for m in range(2, min(nums)):
    tmp, flag = False, True
    for num in nums:
        if tmp is False: tmp = num%m
        elif tmp != num%m:
            flag = False
            break
    if flag:
        res.append(m)
print(*res)