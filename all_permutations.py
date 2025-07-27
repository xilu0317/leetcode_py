def permute(nums: List[int]) -> List[List[int]]:
    res = []
    tmp = []
    used = [False] * len(nums)

    def dfs():
        if len(tmp) == len(nums):
            res.append(tmp.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                tmp.append(nums[i])
                dfs()
                tmp.pop()
                used[i] = False

    dfs()
    
    return res
