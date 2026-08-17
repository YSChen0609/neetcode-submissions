"""
Simply use a max heap with size k
keep pushing the "points" into the heap, if exceeded k, pop the top and keep pushing

This will maintain the top k smallest points

Time: O(nlogk)
Space: O(k)
"""

import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_h = [] # [-dis, px, py]
        
        for px, py in points:
            dis = math.sqrt(px**2+py**2)
            if len(max_h) == k:
                if -max_h[0][0] > dis:
                    # let the new replace the old top
                    hq.heappop(max_h)
                else: continue
            hq.heappush(max_h,[-dis, px, py])
            
            
        res = []
        for _, px, py in max_h:
            res.append([px,py])

        return res