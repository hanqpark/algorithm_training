from itertools import combinations

while True:
    read = input()
    if read == "0": break
    nums = list(map(int, read.split()))
    nums.pop(0)
    for c in combinations(nums, 6):
        print(*c)
    print()