class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        overlap = [intervals[0]]
        for i in range(1, len(intervals)):
            if overlap[-1][1] >= intervals[i][0]:
                overlap[-1][1] = max(intervals[i][1], overlap[-1][1])
            else:
                overlap.append(intervals[i])
        return(overlap)
        