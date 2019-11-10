class Solution:
    def reverseWords(self, s):
        if not s:
            return s

        arr = s.split()
        arr.reverse()

        return ' '.join(arr)
