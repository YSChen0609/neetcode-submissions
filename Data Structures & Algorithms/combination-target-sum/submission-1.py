# backtracking
# 1. sort the nums
# 2. start from smallest, if nums[i] >= target, return
# 3. for each step, decide include or not

# time: O(nlogn + n2**n)
# space: O(n) - extra space


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, comb):
            cur_sum = sum(comb)
            if cur_sum == target:
                res.append(comb.copy())
                return
            
            # less than target, try add others
            for i in range(idx, len(nums)):
                if cur_sum + nums[i] > target: break # exclude those exceeding
                comb.append(nums[i])
                backtrack(i, comb)
                comb.pop()

        backtrack(0, [])

        return res






