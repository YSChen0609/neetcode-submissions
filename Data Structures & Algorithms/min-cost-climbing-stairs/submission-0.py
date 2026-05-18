# dp
# go forward until (top_idx)
# dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
# time: O(N)
# space: O(N) - could be further reduced

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(dp)):
            if i < len(cost):
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2])

        return dp[-1]
