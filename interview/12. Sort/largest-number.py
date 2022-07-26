# https://leetcode.com/problems/largest-number

def largest_number(nums):
    str_nums = map(str, nums)
    res = sorted(str_nums, key=lambda x: x*9, reverse=True)
    return str(int("".join(res)))

def to_swap(n1, n2):
    return str(n1)+str(n2) < str(n2)+str(n1)
    
def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j>0 and to_swap(nums[j-1], nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
    return str(int(''.join(map(str, nums))))


if __name__ == "__main__":
    nums = [[3,30,34,5,9], [999999991, 9]]
    for num in nums:
        res = insertion_sort(nums)
        print(res)