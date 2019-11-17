class Solution:
    def two_sum(self, nums, target):
        dict_ = {}

        for i, x in enumerate(nums):
            if target - x in dict_:
                return [dict_[target - x], i]

            dict_[x] = i

        return None
