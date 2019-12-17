# [TWO-POINTER]
def two_sum_closest(nums, target):
    nums.sort()

    min_ = float('inf')
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            min_ = min(min_, target - nums[left] - nums[right])
            left += 1
        else:
            min_ = min(min_, nums[left] + nums[right] - target)
            right -= 1

    return min_
