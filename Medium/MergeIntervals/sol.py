def merge(intervals: list[list[int]]) -> list[list[int]]:
    res = []
    intervals.sort(key = lambda x: x[0])
    i = 0
    while i < len(intervals):
        j = i
        start = intervals[j][0]
        end = intervals[j][1]

        while j+1 < len(intervals) and intervals[j+1][0] <= end:
            end = max(end,intervals[j+1][1])
            j += 1
        res.append([start,end])
        i = j + 1
    
    return res
                