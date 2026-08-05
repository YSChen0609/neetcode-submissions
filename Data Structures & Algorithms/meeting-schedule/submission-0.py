"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
1. sort the intervals by start
2. if an interval's start < prev interval's end, then there is a conflict

Time: O(nlogn)
Space: O(1)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # edge cases
        if len(intervals) <= 1: return True

        intervals.sort(key=lambda x: x.start)


        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end: return False
        
        return True









