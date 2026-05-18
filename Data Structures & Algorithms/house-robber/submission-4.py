# simply do 2 for-loops
# one for even, one for odd, then compare them
# time: O(n)
# space: O(1)

# but this is not correct!
# e.g. 1, 4, 1, 1, 10, even=12, odd=5, but acutally is 14!
# use dp
# dp[i] = nums[i] + max(dp[0: i-1])
# time: O(n**2)
# space: O(n)

# but this is not optimal!
# think this way: rob this (then you will add to i-2) or 
# not rob this (keep the i-1 best, serve as a record that propergates) 
# then dp[i] = max(nums[i]+dp[i-2], dp[i-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1]




