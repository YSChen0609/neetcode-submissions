# dp
# go forward until (top_idx)
# dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
# time: O(N)
# space: O(N) - could be further reduced
# reduce space complexity:
# curr = min(prev_1, prev_2) + cost[i]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # target step costs nothing
        dp = [0] * (len(cost))
        prev_2, prev_1 = cost[0], cost[1]

        for i in range(2, len(dp)):
            curr = min(prev_2, prev_1) + cost[i]
            prev_2, prev_1 = prev_1, curr

        return curr
