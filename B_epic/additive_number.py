class Solution(object):
    # KEY: find the first two sequence and then check the remaining
    def is_additive_number(self, num):
        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i >= 2:
                return False

            for j in range(i + 1, min(n - i, (n + i) // 2) + 1):
                if num[i] == '0' and j - i >= 2:
                    '''
                        If the current sequence starts with 0, then no need to consider the sequence further.
                        But the string could still be valid (as trailing 0) so don't return false
                    '''
                    break

                num1 = num[:i]
                num2 = num[i:j]
                remain = num[j:]

                if self.is_valid(num1, num2, remain):
                    return True

        return False

    def is_valid(self, num1, num2, remain):
        if remain == '':
            return True

        sum_ = str(int(num1) + int(num2))

        if remain.startswith(sum_):
            return self.is_valid(num2, sum_, remain[len(sum_):])
        else:
            return False
