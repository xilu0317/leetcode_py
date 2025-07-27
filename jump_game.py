#GREEDY

def canJump(nums: List[int]) -> bool:
    maxReach = 0

    for i, jump in enumerate(nums):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + jump)

    return True
