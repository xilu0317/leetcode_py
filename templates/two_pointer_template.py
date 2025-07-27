def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) - 1
    
    while l < r:
        curSum = arr[l] + arr[r]
        if curSum == target:
            return [l+1, r+1]  # 1-indexed result
        elif curSum < target:
            l += 1
        else:
            r -= 1

    return []
