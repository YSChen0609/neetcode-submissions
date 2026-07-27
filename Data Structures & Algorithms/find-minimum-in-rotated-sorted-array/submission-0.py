"""
We wanna use binary search to achieve O(logn)
There are only 2 possibilities:
(larger->max)(min->large) / (min->large)

l, m, r
if nums[m]>nums[r] => search m+1:r
else => search l:m
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]



