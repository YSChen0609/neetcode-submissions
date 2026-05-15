# backtracking
# [1, 1, 1] -> 1, 11, 111
# use a set to avoid duplicates
# time: O(n*n**2)
# space: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def backtrack(idx: int,sub: List)->List[int]:
            if idx == len(nums):
                res.add(tuple(sub)) 
                return
            
            # option 1: add current
            sub.append(nums[idx])
            backtrack(idx+1, sub)
            sub.pop()

            # option 2: skip current
            backtrack(idx+1, sub)
        
        backtrack(0, [])
        # cast res to list
        return [list(sub) for sub in res]