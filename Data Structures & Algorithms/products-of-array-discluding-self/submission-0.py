# prefix prod and postfix prod
# 1. loop forward to get prefix prod (x)
# 2. loop backward to get postfix prod (y)
# 3. for idx i, res[i] =  x[i-1] * y[i+1] 
# time: O(n)
# space: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [nums[0]] * n
        post_prod = [nums[-1]] * n
        # 1. loop forward to get prefix prod (x)
        # [1, 2, 8, 48]
        for i in range(1, n):
            pre_prod[i] = nums[i] * pre_prod[i-1]
        # 2. loop backward to get postfix prod (y)
        # [48, 48, 24, 6]
        for i in range(n-2, -1, -1):
            post_prod[i] = nums[i] * post_prod[i+1]
        # 3. get res
        res = [1] * n
        res[0], res[-1] = post_prod[1], pre_prod[n-2]
        for i in range(1, n-1):
            res[i] = pre_prod[i-1] * post_prod[i+1]

        return res
        
