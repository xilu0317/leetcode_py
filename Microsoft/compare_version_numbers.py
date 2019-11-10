class Solution:
    def compare_version(self, v1, v2):
        l1, l2 = v1.split('.'), v2.split('.')

        l1 = list(map(lambda x: int(x), l1))
        l2 = list(map(lambda x: int(x), l2))

        minLen = len(l1) if len(l1) < len(l2) else len(l2)
        maxLen = len(l1) if len(l1) > len(l2) else len(l2)

        for i in range(minLen):
            if l1[i] < l2[i]:
                return -1
            if l1[i] > l2[i]:
                return 1

        j = minLen
        while j < maxLen:
            if j >= len(l1) and l2[j] > 0:
                return -1
            if j >= len(l2) and l1[j] > 0:
                return 1
            j += 1

        return 0
