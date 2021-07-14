"""
Medium 253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key=lambda x: x.start)
        end_ts = []
        heapify(end_ts)
        for meeting in intervals:
            if not end_ts or end_ts[0] > meeting.start:
                heappush(end_ts, meeting.end)

            else:
                heappop(end_ts)
                heappush(end_ts, meeting.end)
        return len(end_ts)
