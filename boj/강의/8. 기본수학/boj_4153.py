while True:
    nums = list(map(int, input().split()))
    z = max(nums)
    if not z: break
    nums.pop(nums.index(z))
    print("right" if nums[0]*nums[0]+nums[1]*nums[1]==z*z else "wrong")