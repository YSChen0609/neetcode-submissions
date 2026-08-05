"""
classic question.

Note that the "subseq" is NOT contigious, so the sliding window doesn't work.
Use DP instead.

Let dp[i] represents the len of LIS until i, i.e. nums[:i+1]

so:

dp[i] = 1+ max(dp[k]) for all num[k] < nums[i] else 1 (starting fresh)

Time: O(n**2)
Space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)

        for i, n in enumerate(nums[1:], start=1):
            max_prev = 1
            for j in range(i):
                if n > nums[j]:
                    max_prev = max(max_prev, lis[j]+1)
            lis[i] = max(1, max_prev)

        return max(lis)
            











        