"""
We basically need to keep a ds which can easily give use a pq with indexing
first idea: max heap
Time: O(nlogn + klogn)
Space: O(n)

Second idea: min heap + length check 
keep pushing into the min heap, so the top to bottom will be small to large
and since I maintain a size of k, and pop whenever there is a larger value than the top wants to get in, we pop the top

so the min heap will have the top-k largest of all stream, with the top being the k-th largest

Time: O(nlogk)
Space: O(k)
"""

import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums
        hq.heapify(self.pq) # O(n)
        # maintain a size of k
        while self.pq and len(self.pq) > k:
            hq.heappop(self.pq)
            
    def add(self, val: int) -> int:
        
        hq.heappush(self.pq,val)
        while len(self.pq) > self.k:
            hq.heappop(self.pq)
        
        return self.pq[0]



