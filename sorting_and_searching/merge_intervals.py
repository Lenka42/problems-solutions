from typing import List


# brut force
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx1 = 0
        while idx1 < len(intervals):
            interval1 = intervals[idx1]
            idx2 = idx1 + 1
            while idx2 < len(intervals):
                interval2 = intervals[idx2]
                if interval1[0] <= interval2[1] and interval1[1] >= interval2[0]:
                    merged_interval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
                    intervals[idx1] = merged_interval
                    interval1 = merged_interval
                    del intervals[idx2]
                    idx2 = idx1 + 1
                else:
                    idx2 += 1
            idx1 += 1
        return intervals


# sort first
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
