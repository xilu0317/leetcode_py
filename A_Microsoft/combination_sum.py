class Solution:
    # standard backtracking
    def combination_sum(self, candidates, target):
        res = []
        self.dfs(candidates, target, 0, [], res)

        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking

        if target == 0:
            res.append(path)
            return  # backtracking

        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


class Solution:
    # faster
    def combination_sum(self, candidates, target):
        res = []
        candidates = sorted(candidates)

        def dfs(remain, arr):
            if remain == 0:
                res.append(arr)
                return

            for x in candidates:
                if x > remain:
                    break

                if arr and x < arr[-1]:  # '-1' means last element in the array
                    continue
                else:
                    dfs(remain - x, arr + [x])

        dfs(target, [])

        return res
