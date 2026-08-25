class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]

        for i in range(len(intervals)):

            # New interval overlaps this interval
            if start <= intervals[i][1]:
                j = i

                while j < len(intervals) and intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                    j += 1

                intervals[i:j] = [[min(intervals[i][0], start), end]]
                return intervals

            # New interval goes before this interval
            elif end < intervals[i][0]:
                intervals[i:i] = [[start, end]]
                return intervals

        # New interval goes at the end
        intervals.append([start, end])
        return intervals



                 

