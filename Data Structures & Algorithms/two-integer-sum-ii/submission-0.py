# idea: sorted, use 2-ptrs
# l = 1, r = len(numbers)-1
# 1. if sum > target: r-=1
# 2. else: l += 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1 # start using 0-idx, change later

        while l<r:
            if numbers[l]+numbers[r] == target: break
            elif numbers[l]+numbers[r] > target: r -= 1
            else: l += 1
        
        return [l+1, r+1] # modify to 1-indexed

