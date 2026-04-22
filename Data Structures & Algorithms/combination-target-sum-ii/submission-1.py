# c > 30 shall not be considered
# sort the array, trunc c> 30 -> [1:30]
# n, [n+1: 30] -> n, n+1 [n+2:30]
# time: O(2**n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the cand.
        # [comb] , idx
        candidates.sort()
        self.res = []

        def backtrack(last_idx, curr_comb:List):
            # if not curr_comb: curr_sum = candidates[idx]
            # else: curr_sum = sum(curr_comb) + candidates[idx]

            if curr_comb: curr_sum = sum(curr_comb)
            else: curr_sum = 0
            if curr_sum == target:
                # print("A")
                self.res.append(curr_comb.copy())
                return
            elif curr_sum < target: # [1, 2, 3]
                for i in range(last_idx+1, len(candidates)):
                    if candidates[i] > 30: break
                    if i != last_idx+1 and candidates[i] == candidates[i-1]: continue
                    curr_comb.append(candidates[i])
                    backtrack(i, curr_comb) 
                    curr_comb.pop()
            else:
                return
        
        backtrack(-1,[])
        # res = [list(x) for x in set(self.res)]
        return self.res


