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




