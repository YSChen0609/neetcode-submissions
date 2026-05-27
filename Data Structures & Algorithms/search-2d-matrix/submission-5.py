"""
sorted, view it as a bin-search problem

To get the mid, i.e., halve every time, we use:
- init: lo, hi = 0, m*n-1 (re-indexed)
- each iteration: mid = lo+hi//2 + 1
- mid_idx = mid//n, mid%n / m

m, n = 3, 4
mid = 3 -> (0, 3)
mid//n = 1
mid%n = 1


time: O(log(m*n))
space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge cases
        if target < matrix[0][0] or target > matrix[-1][-1]: 
            return False
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1
        
        if matrix[lo//n][lo%n] == target: return True
        if matrix[hi//n][hi%n] == target: return True
        while lo < hi:
            mid = (lo+hi)//2
            mid_val = matrix[mid//n][mid%n]
            if mid_val == target: return True
            elif mid_val > target: hi = mid
            else: lo = mid+1
        
        return False





