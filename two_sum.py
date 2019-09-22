class Solution:
    def twoSum(self, nums, target):
        if (not nums or not len(nums)):
            return -1

        dict = {}

        for i, num in enumerate(nums):
            if target - num in dict:
                return ([dict[target - num], i])
            dict[num] = i

        return -1
