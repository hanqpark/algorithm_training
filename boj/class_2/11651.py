import sys
read = sys.stdin.readline
nums = [list(map(int, read().split())) for _ in range(int(read()))]
for x, y in sorted(nums, key=lambda x: (x[1], x[0])):
    print(x, y)