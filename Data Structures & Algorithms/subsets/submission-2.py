"""
Backtracking

for each pass, decide to include the curr num or not

time: O(2**n)
space: O(n) for the call stack
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def appending(path: List[int], idx: int) -> List[int]:
            if idx >= N:
                res.append(path.copy())
                return
            
            # choice 1: include curr
            path.append(nums[idx])
            appending(path, idx+1)

            # choice 2: exclude curr
            path.pop()
            appending(path, idx+1)
        
        appending([], 0)

        # return [list(x) for x in res]
        return res





