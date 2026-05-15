# backtracking
# use the nums list itself
# form the perm step by step until len(perm) == len(nums)
# for each step, pick a num and append it, then pop it from the list

# time: O(n*n!)
# space: O(n) - extra space (call stack)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)

        def backtrack(perm, n_list):
            if len(perm) == l:
                res.append(perm.copy())
                return

            for i, n in enumerate(n_list):
                perm.append(n)
                n_list.pop(i)

                backtrack(perm,n_list)
                
                n_list.insert(i, n)
                perm.pop()

        backtrack([], nums)
        return res





