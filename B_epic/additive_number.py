class Solution(object):
    def isAdditiveNumber(self, num):
        # Idea: find the first 2 strings and then continue to check the remaining strings
        n = len(num)
        # 1st number is num[0:i], 2nd number is num[i:j]
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i >= 2:
                break

            for j in range(i + 1, min(n - i, (n + i) // 2) + 1):
                if num[i] == '0' and j - i >= 2:
                    break  # means starting with "0", e.g., "03"
                num1 = num[0:i]
                num2 = num[i:j]
                remain = num[j:]

                if self.is_valid(num1, num2, remain):
                    return True

        return False

    def is_valid(self, num1, num2, remain):
        if remain == '':    # means checked whole string
            return True

        total = str(int(num1) + int(num2))

        if remain.startswith(total):
            return self.is_valid(num2, total, remain[len(total):])
        else:
            return False
