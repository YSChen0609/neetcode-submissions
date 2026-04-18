# use dp
# dp[i] = distinct ways to climb from 0 to staircase i
# dp[i] = dp[i-1] + dp[i-2]
class Solution:
    def climbStairs(self, n: int) -> int:
        # edge cases
        if n <= 2: return n
        # init dp
        dp = [1] * (n+1) # 0-n
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]