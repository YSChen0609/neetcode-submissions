# do a binary search
# time: O(logn)
# space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        if nums[lo] == target: return lo
        if nums[hi] == target: return hi
        
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == target: return mid
            elif nums[mid] > target: hi = mid
            else: lo = mid+1
        
        # cannot find
        return -1