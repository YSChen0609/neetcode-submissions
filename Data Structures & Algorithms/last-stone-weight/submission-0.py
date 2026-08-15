"""
Need a priority queue: use max heap

pop the top 2, then push the new weight 
until the size == 1

Time: O(nlogn)
Space: O(n)
"""
import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        hq.heapify_max(stones)
        while len(stones) > 1:
            first = hq.heappop_max(stones)
            second = hq.heappop_max(stones)
            hq.heappush_max(stones, first-second)

        return stones[0]
