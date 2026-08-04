"""
Use dp, with the relationship func: dp[i] = max(nums[i]+dp[i-2], dp[i-1])
that is, rob i and with dp[i-2] or NOT ROB i and inherit the dp[i-1]
with dp[i] representing the max rob amount we can rob nums[:i+1]

with a twist:
if we rob nums[0], we can only rob until nums[-2]
so we can do a rob[0:n] (exclude the last house) vs rob[1:] (exclude the first house)

then:

Time: O(n)
Space: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        # candidate: 0:n
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for v in nums[2:len(nums)-1]:
            rob1, rob2 = rob2, max(rob2, v+rob1)
        
        can1 = rob2

        # candidate: 1:
        """
        r1, r2 = 12, 
        """
        rob1, rob2 = nums[1], max(nums[1], nums[2])
        for v in nums[3:len(nums)]:
            rob1, rob2 = rob2, max(rob2, v+rob1)
        
        can2 = rob2

        return max(can1, can2)




        