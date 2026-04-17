# since choosing diff pairs of bars could lead to any relationship with the prev case, we have to "test every possibilities".
# Notice that the width be shrinking when we move bars inwards, we can start from the widest pairs.
# If we want to possibly find max, we move the shortest bar since the area is decided by it.
# This is a heuristic way to better the max_
# Time: O(n)
# space: O(1) 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(l, r):
            return min(heights[l], heights[r]) * (r-l)

        l, r = 0, len(heights)-1
        res = 0

        while l != r:
            res = max(res, getArea(l, r))
            if heights[l] > heights[r]: r -= 1
            else: l += 1
        return res




