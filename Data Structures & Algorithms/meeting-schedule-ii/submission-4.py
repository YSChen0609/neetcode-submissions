"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Method 1:
After sorted the intervals,
check if there is conflict, if there is, add another room,
else update the ending time of the room,

so we use a heap to maintain the min. end time, and update the end time for each room

Time: O(nlogn)-sorting and heappop and heappush
Space: O(n)
"""
import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start,x.end))
        res = 0
        h = []

        for m in intervals:
            if h and h[0] <= m.start:
                hq.heappop(h)
            hq.heappush(h, m.end)
            res = max(res, len(h))
        
        return res
            






        