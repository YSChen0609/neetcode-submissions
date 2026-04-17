# use a hashmap (set) to allocate existing ones
# encounter an existing one, return T
# time: O(n)
# space: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for n in nums:
            if n in existing:
                return True
            else:
                existing.add(n)
        
        # if not returned yet, no duplicates
        return False