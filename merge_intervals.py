class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []

        for current_interval in intervals:
            # Get start and end of current interval
            start, end = current_interval
            
            # If merged_intervals is not empty and current interval overlaps
            if merged_intervals and start <= merged_intervals[-1][1]:
                # Merge by updating the end time
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                # No overlap, add current interval to result
                merged_intervals.append(current_interval)
        
        return merged_intervals