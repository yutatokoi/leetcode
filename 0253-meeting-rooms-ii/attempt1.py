class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starting_times = sorted(i[0] for i in intervals)
        ending_times = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if starting_times[s] < ending_times[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res

        
