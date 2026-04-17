# 1. trav the nums once to get distinct values, put them into dict{num: longest_consecutive_len(default=1)}
# 2. from the smallest one, gradually update the longest count per num
# 3. cnt[num] = max(cnt[num-1] + 1, 1)
# 4. also maintain the longest
# time: O(n)
# space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) <= 1: return len(nums)

        # put distinct nums in the dict, with default cnt = 1
        distinct_nums = {} # num -> longest_consecutive_len ends with n
        for n in nums: distinct_nums[n] = 1

        res = 1
        for n in range(min(nums), max(nums)+1):
            if n not in distinct_nums: continue
            distinct_nums[n] = distinct_nums.get(n-1, 0)+1
            res = max(res, distinct_nums[n])

        return res
            