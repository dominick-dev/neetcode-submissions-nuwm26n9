"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by start
        intervals.sort(key=lambda i: i.start)

        # iterate through from first
        for i in range(1, len(intervals)):
            # if curr and prev interval overlap
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
