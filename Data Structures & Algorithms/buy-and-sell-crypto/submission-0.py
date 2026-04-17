# idea: find the "smallest on left and largest on right"
# 1. use prefix-min and suffix-max
# 2. subtract the two, the max profit is gotten
# time: O(n)
# space: O(n)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_ = prices[0]
        max_ = prices[-1]
        pre_min = [prices[0]] * n
        suf_max = [prices[-1]] * n
        # get pre_min
        for i in range(1,n):
            min_ = min(min_, prices[i])
            pre_min[i] = min_
        # get suf_max
        for i in range(n-2,-1,-1):
            max_ = max(max_, prices[i])
            suf_max[i] = max_
        
        res = 0
        for m, n in zip(pre_min, suf_max):
            if n-m > res: res = n-m
        
        return res
