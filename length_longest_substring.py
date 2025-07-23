class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = max_len = 0

        for right, c in enumerate(s):
            if c in char_index and char_index[c] >= left:
                left = char_index[c] + 1
            char_index[c] = right
            max_len = max(max_len, right - left + 1)

        return max_len