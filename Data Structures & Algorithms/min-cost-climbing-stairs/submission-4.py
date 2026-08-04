"""
Use Dp as:

dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

and we can lower the mem. cost by storing just 2 values

Time: O(n)
Space: O(1)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = 0, 0

        cost.append(0) # extend the list for simplier cal.

        for i in range(2, len(cost), 1):
            dp1, dp2 = dp2, min(dp1+cost[i-2],dp2+cost[i-1])
        
        return dp2



