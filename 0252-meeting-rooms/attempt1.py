class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x[0])

        prev_end = intervals[0][1]

        for start, end in intervals:
            if start < prev_end:
                return False
            prev_end = end

        return True


