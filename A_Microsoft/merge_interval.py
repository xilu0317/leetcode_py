class Solution:
    def merge(self, intervals):
        if not intervals:
            return None

        intervals = sorted(intervals, key=lambda x: x[0])

        res, pre = [], intervals[0]

        # exclude the first term here
        for x in intervals[1:]:
            if pre[1] >= x[0]:
                pre[1] = max(pre[1], x[1])
            else:
                res.append(pre)
                pre = x

        res.append(pre)

        return res