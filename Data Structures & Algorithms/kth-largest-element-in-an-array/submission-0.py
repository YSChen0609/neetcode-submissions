"""
Maintain a min-heap with size of k
which represents the k largest ones

whenever the size of the h exceeds k, we pop the top (smallest among them)

Time: O(nlogk)
Space: O(k)
"""

import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_h = []
        for n in nums:
            hq.heappush(min_h, n)
            if len(min_h) > k:
                hq.heappop(min_h)
        
        return min_h[0]