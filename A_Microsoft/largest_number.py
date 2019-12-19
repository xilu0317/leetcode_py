from functools import cmp_to_key


class Solution:
    def largest_number(self, nums):
        output = [str(x) for x in sorted(nums, key=cmp_to_key(self.comp))]

        if all(x == '0' for x in output):
            return '0'

        return ''.join(output)

    # KEY
    def comp(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        else:
            return 1
