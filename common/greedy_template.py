def can_jump(nums: List[int]) -> bool:
    maxReach = 0
    
    for i, jump in enumerate(nums):
        if i > maxReach:
            return False      # if current index is not reachable
        maxReach = max(maxReach, i + jump)

    return True
