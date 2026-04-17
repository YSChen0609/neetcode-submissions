# idea: no need to return idx (just vals), use sorted array
# sorted = [-4, -1, -1, 0, 1, 2]
# 1. for n in sorted: find the sum to complimentary
# 2. no need to consider prev ones (sub-array shrinks)
# time: O(nlogn + n**2)
# space: O(1) for ptrs

class Solution:
    ans = []

    def find_tris_from_x(self, nums, i):
        # find the ones that compliment nums[i]
        l, r = i+1, len(nums)-1
        while l<r:
            if nums[l] + nums[r] == -nums[i]: 
                if [nums[i], nums[l], nums[r]] not in self.ans:
                    self.ans.append([nums[i], nums[l], nums[r]])
                    l += 1
            if nums[l] + nums[r] > -nums[i]: r -= 1
            else: l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        for i in range(len(nums)):
            tris = self.find_tris_from_x(nums, i)

        return self.ans