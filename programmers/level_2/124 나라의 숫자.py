def solution(n):
    ans = []
    nums = ["4", "1", "2"]
    while n:
        tmp = n%3
        ans.append(nums[tmp])
        if not tmp:
            n = n//3-1
        else:
            n//=3
    return "".join(reversed(ans))