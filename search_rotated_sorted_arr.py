def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        # Check if left half is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # Otherwise, right half must be sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1
