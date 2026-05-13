# backtracking
# decide include nums[i] or not
# time: O(n*2**n) - n for copy
# space: O(n)-call stack

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curList: List, curIdx:int) -> List:
            
            if curIdx == len(nums): 
                res.append(curList.copy())
                return

            # choice 1: don't add curIdx to list
            backtrack(curList, curIdx+1)

            # choice 2: add curIdx to list
            curList.append(nums[curIdx])
            backtrack(curList, curIdx+1)
            curList.pop()

        backtrack([],0)

        return res

                
