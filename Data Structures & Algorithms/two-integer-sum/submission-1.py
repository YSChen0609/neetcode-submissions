# use a hashmap: dict{target-cur_val: cur_idx}
# trav the nums once
# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                return [hashmap[n], i]
            else:
                hashmap[target-n] = i