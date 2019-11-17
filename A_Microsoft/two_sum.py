class Solution:
    def two_sum(self, nums, target):
        _dict = {}

        for i, x in enumerate(nums):
            if target - x in _dict:
                return [_dict[target - x], i]
            _dict[x] = i

        return None
