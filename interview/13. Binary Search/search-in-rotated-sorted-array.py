# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

def search(nums: List[int], target: int):
    try:
        return nums.index(target)
    except:
        return -1
    
def binary_search(nums, target):
        if not nums: return -1
        
        # 최솟값을 찾아 pivot 설정
        l, r = 0, len(nums)-1
        while l < r:
            mid = l+(r-l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        pivot = l
        
        # pivot 기준 이진 검색
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+(r-l)//2
            mid_pivot = (mid+pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                l = mid+1
            elif nums[mid_pivot] > target:
                r = mid-1
            else:
                return mid_pivot
        return -1
    

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    res = binary_search(nums, 4)
    print(res)