"""
Idea: Use DP
dp[i] represents the LIS ending on i
and dp[i] = max(1, dp[j]+1) for nums[j]<nums[i] and j<i

Time: O(n)
Space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])

        print(dp)
        return max(dp)
            
        