"""
O(n) is obvious, aka linear search

Sorted (in some way) -> binary search O(logn)

we start from l = 0, r = 5
if mid > r: then we know that mid is at the "Left portion"
else: we know mid in the "Right portion)

[4,5,6,7,1,2,3]
 l       t m r
 
But how about the target?
1. mid in L portion (mid > l)
    if target > mid: target must in L and to the right of mid -> search (right of mid)
    if l < t : target must in L and to the left of mid -> search (left of mid)
    if t < l : target must in R -> search (right of mid)

    =>
    if t > m or t < l: search (right of mid)
    else: search (left of mid)

2. mid in R portion (mid < r)
    if target < mid: target must in R and to the left of mid -> search (left of mid)
    if r < t: target must in L and to the left of mid -> search (left of mid)
    if t < r: target must in R -> search (right of mid)

    =>
    if t < mid or r < t: search (left of mid)
    else search (right of mid)

Time: O(logn)
Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target: return mid

            if nums[mid] > nums[r]: # now mid in L
                if target > nums[mid] or target < nums[l]: l = mid + 1 # search right
                else: r = mid -1
            
            else: # now mid in R
                if target < nums[mid] or target > nums[r]: r = mid -1 # search left
                else: l = mid + 1

        return -1














