class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        res = []

        for current_interval in intervals:
            start, end = current_interval # unpacking
            
            if res and start <= res[-1][1]:
                # Merge by updating the end time
                res[-1][1] = max(res[-1][1], end)
            else:
                # No overlap, add current interval to result
                res.append(current_interval)
        
        return res


# unpacking examples
# Basic unpacking with two values
numbers = [5, 10]
start, end = numbers    # start = 5, end = 10
 
# last val example
arr = [1, 2, 3, 4, 5]
last = arr[-1]      # 5  (last element)
second_last = arr[-2]  # 4  (second to last)